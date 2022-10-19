from abi.chain_link.MockV3Aggregator import MockV3Aggregator
from fund.models import Asset
from management.models import PriceManagement
from utils.data_source.ftx.utils import add_asset_price_to_db, get_price_from_ftx
from utils.multicall.multicall import Multicall
from utils.multicall.multicall_write import MulticallWrite
from utils.utils import get_provider


def manage_price_feed():
    w3 = get_provider()
    multicall_write = MulticallWrite(w3, "fuji")
    targets = list(Asset.objects.all())
    update_answer_calls = []
    for target in targets:
        # get price
        data = get_price_from_ftx(target.ftx_pair_name, target.is_short_position)
        mock_v3_aggregator = w3.eth.contract(
            target.price_feed,
            abi=MockV3Aggregator,
        )
        if target.is_short_position:
            data = int(10000 * 1e8 / data)
        else:
            data = int(data * 1e8)
        if target.address == "0x9a13BE5e8D310C07BF4dBE7Dc4CF5b699AA5430a":
            data = 1 * 1e8
        if target.price_feed_is_mocked:
            update_answer_calls.append(
                multicall_write.create_call(
                    mock_v3_aggregator,
                    "updateAnswer",
                    [int(data)],
                ),
            )

    multicall_write.call(update_answer_calls)


manage_price_feed()
