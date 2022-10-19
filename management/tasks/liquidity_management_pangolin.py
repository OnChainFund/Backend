from math import sqrt

from eth_utils.address import to_canonical_address
from web3.contract import Contract

from abi.others.ERC20 import ERC20 as ERC20_ABI
from abi.others.PangolinRouter import PangolinRouter
from management.models import PriceManagement
from utils.constants.addresses import addresses
from utils.data_source.ftx.utils import get_price_from_ftx
from utils.multicall.multicall import Multicall
from utils.multicall.multicall_write import MulticallWrite
from utils.utils import get_provider


def liquidity_management_pangolin():
    w3 = get_provider()

    multicall = Multicall(w3, "fuji")
    multicall_write = MulticallWrite(w3, "fuji")
    targets = list(PriceManagement.objects.all())
    approve_erc20_calls = []
    pangolin_liquidity_get_pair_reserve_calls = []
    pangolin_liquidity_management_calls = []
    ftx_prices = []
    pangolin_router: Contract = w3.eth.contract(
        addresses["pangolin"]["Router"], abi=PangolinRouter
    )
    multicall_address = "0xcA11bde05977b3631167028862bE2a173976CA11"
    # get pair
    # get balance
    for target in targets:
        ftx_prices.append(
            get_price_from_ftx(target.ftx_pair_name, target.is_short_position)
        )
        print(target.pangolin_pool_address)
        target_asset = w3.eth.contract(
            address=to_canonical_address(target.target_asset.address), abi=ERC20_ABI
        )
        denominated_asset = w3.eth.contract(
            address=to_canonical_address(target.denominated_asset.address),
            abi=ERC20_ABI,
        )
        pangolin_liquidity_get_pair_reserve_calls.append(
            multicall.create_call(
                target_asset,
                "balanceOf",
                [target.pangolin_pool_address],
            ),
        )

        pangolin_liquidity_get_pair_reserve_calls.append(
            multicall.create_call(
                denominated_asset,
                "balanceOf",
                [target.pangolin_pool_address],
            ),
        )

        result = multicall.call(pangolin_liquidity_get_pair_reserve_calls)

        # calculate swap info
        for i in range(0, len(targets)):
            target = targets[i]
            target_asset_reserve = int(result[1][2 * i].hex(), 16)  # type: ignore
            denominated_asset_reserve = int(result[1][2 * i + 1].hex(), 16)  # type: ignore
            pangolin_price = denominated_asset_reserve / target_asset_reserve
            ftx_price = ftx_prices[i]
            if pangolin_price < ftx_price:
                # print("buy target")
                # print(sqrt(target_asset_reserve * denominated_asset_reserve * ftx_price))
                # print(target_asset_reserve)
                amount = (
                    sqrt(target_asset_reserve * denominated_asset_reserve * ftx_price)
                    - denominated_asset_reserve
                )
                path = [target.denominated_asset.address, target.target_asset.address]
            else:
                # print("sell target")
                # print(sqrt(target_asset_reserve * denominated_asset_reserve * ftx_price))
                # print(target_asset_reserve)
                amount = denominated_asset_reserve - sqrt(
                    target_asset_reserve * denominated_asset_reserve * ftx_price
                )
                path = [target.target_asset.address, target.denominated_asset.address]
            print(int(abs(amount)))
            send_asset = w3.eth.contract(
                address=to_canonical_address(path[0]), abi=ERC20_ABI
            )
            pangolin_liquidity_management_calls.extend(
                [
                    multicall.create_call(
                        send_asset,
                        "transferFrom",
                        [
                            addresses["user_1"],
                            multicall_address,
                            int(abs(amount)),
                        ],  # _from,_to,_value
                    ),
                    multicall.create_call(
                        pangolin_router,
                        "swapExactTokensForTokens",
                        [
                            int(abs(amount)),
                            1,
                            path,
                            addresses["user_1"],
                            1758392484,
                        ],
                    ),
                ]
            )
        result = multicall_write.call(pangolin_liquidity_management_calls)


liquidity_management_pangolin()
