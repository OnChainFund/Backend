from abi.others.ERC20 import ERC20 as ERC20_ABI
from abi.others.PangolinRouter import PangolinRouter
from management.models import PriceManagement
from utils.constants.addresses import addresses
from utils.data_source.ftx.utils import get_price_from_ftx
from utils.multicall.multicall import Multicall
from utils.multicall.multicall_write import MulticallWrite
from utils.utils import get_provider

w3 = get_provider()

multicall = Multicall(w3, "fuji")
multicall_write = MulticallWrite(w3, "fuji")
targets = list(PriceManagement.objects.all())
approve_erc20_calls = []
pangolin_liquidity_get_pair_reserve_calls = []
pangolin_liquidity_management_calls = []
ftx_prices = []
pangolin_router = w3.eth.contract(addresses["pangolin"]["Router"], abi=PangolinRouter)

# get pair
# get balance
for target in targets:
    if target.ftx_pair_name is not None:
        ftx_prices.append(
            get_price_from_ftx(target.ftx_pair_name, target.is_short_position)
        )
        print(target.pangolin_pool_address)
        target_asset = w3.eth.contract(address=target.target_asset.address, abi=ERC20_ABI)  # type: ignore
        denominated_asset = w3.eth.contract(
            address=target.denominated_asset.address, abi=ERC20_ABI  # type: ignore
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
    target_asset_reserve = int(result[1][2 * i].hex(), 16)
    denominated_asset_reserve = int(result[1][2 * i + 1].hex(), 16)
    pangolin_price = denominated_asset_reserve / target_asset_reserve
    print(target)
    print(pangolin_price)
