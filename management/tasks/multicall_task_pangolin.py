from math import sqrt
from contract.contracts.deployment.others.Addresses import Addresses
from contract.contracts.deployment.others.PangolinRouter import PangolinRouter
from management.models import PriceManagement
from management.tasks.utils import get_price_from_ftx
from utils.multicall.multicall_write import MulticallWrite
from utils.utils import get_provider
from utils.multicall.multicall import Multicall
from contract.contracts.deployment.others.ERC20 import ERC20 as ERC20_ABI

w3 = get_provider()

multicall = Multicall(w3, "fuji")
multicall_write = MulticallWrite(w3, "fuji")
targets = list(PriceManagement.objects.all())
approve_erc20_calls = []
pangolin_liquidity_get_pair_reserve_calls = []
pangolin_liquidity_management_calls = []
ftx_prices = []
pangolin_router = w3.eth.contract(Addresses["pangolin"]["Router"], abi=PangolinRouter)
# get pair
# get balance
for target in targets:
    ftx_prices.append(
        get_price_from_ftx(target.ftx_pair_name, target.is_short_position)
    )
    print(target.pangolin_pool_address)
    target_asset = w3.eth.contract(address=target.target_asset.address, abi=ERC20_ABI)
    denominated_asset = w3.eth.contract(
        address=target.denominated_asset.address, abi=ERC20_ABI
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
    approve_erc20_calls.append(
        multicall_write.create_call(
            target_asset,
            "approve",
            [pangolin_router.address, int(1e30)],
        ),
    )
result = multicall.call(pangolin_liquidity_get_pair_reserve_calls)


# calculate swap info
for i in range(0, len(targets)):
    target = targets[i]
    target_asset_reserve = int(result[1][2 * i].hex(), 16)
    denominated_asset_reserve = int(result[1][2 * i + 1].hex(), 16)
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
    pangolin_liquidity_management_calls.append(
        multicall.create_call(
            pangolin_router,
            "swapExactTokensForTokens",
            [
                int(1e5),
                1,
                path,
                Addresses["user_1"],
                1758392484,
            ],
        ),
    )
result = multicall_write.call([pangolin_liquidity_management_calls[1]])
# print(result)