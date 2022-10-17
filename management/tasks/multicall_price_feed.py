from abi.chain_link.MockV3Aggregator import MockV3Aggregator
from management.models import PriceManagement
from utils.data_source.ftx.utils import (add_asset_price_to_db,
                                         get_price_from_ftx)
from utils.multicall.multicall import Multicall
from utils.multicall.multicall_write import MulticallWrite
from utils.utils import get_provider


def manage_price_feed():
    w3 = get_provider()

    multicall_write = MulticallWrite(w3, "fuji")
    multicall_read = Multicall(w3, "fuji")
    targets = list(PriceManagement.objects.all())
    update_answer_calls = []
    pangolin_pair_info_calls = []
    pangolin_liquidity_managemeny_calls = []
    for target in targets:
        # get price
        data = get_price_from_ftx(target.ftx_pair_name, target.is_short_position)
        mock_v3_aggregator = w3.eth.contract(
            target.target_asset.price_feed,
            abi=MockV3Aggregator,
        )

        if target.update_asset_price_mock_v3_aggregator:
            update_answer_calls.append(
                multicall_write.create_call(
                    mock_v3_aggregator,
                    "updateAnswer",
                    [int(data * 1e8)],
                ),
            )
        if target.update_asset_price_db:
            add_asset_price_to_db(target.target_asset.address, data)

    multicall_write.call(update_answer_calls)
