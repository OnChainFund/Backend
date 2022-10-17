from abi.others.ERC20 import ERC20 as ERC20_ABI
from abi.others.PangolinRouter import PangolinRouter
from fund.models import Asset
from utils.constants.addresses import addresses
from utils.multicall.multicall import Multicall
from utils.multicall.multicall_write import MulticallWrite
from utils.utils import get_provider

w3 = get_provider()

multicall = Multicall(w3, "fuji")
multicall_write = MulticallWrite(w3, "fuji")
targets = list(Asset.objects.all())
approve_erc20_calls = []
pangolin_liquidity_get_pair_reserve_calls = []
pangolin_liquidity_management_calls = []
ftx_prices = []
pangolin_router = w3.eth.contract(addresses["pangolin"]["Router"], abi=PangolinRouter)
# get pair
# get balance
for target in targets:

    target_asset = w3.eth.contract(address=target.address, abi=ERC20_ABI)

    approve_erc20_calls.append(
        multicall_write.create_call(
            target_asset,
            "approve",
            [pangolin_router.address, int(1e30)],
        ),
    )
result = multicall_write.call(approve_erc20_calls)
