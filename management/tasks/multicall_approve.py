from eth_utils.address import to_canonical_address
from abi.others.ERC20 import ERC20 as ERC20_ABI
from abi.others.PangolinRouter import PangolinRouter
from fund.models import Asset
from utils.constants.addresses import addresses
from utils.multicall.multicall import Multicall
from utils.multicall.multicall_write import MulticallWrite
from utils.utils import get_provider


def approve_multicall_contract_to_use_all_asset_in_wallet():
    """approve multicall contract to use all assets (in asset DB) of the user wallet"""
    w3 = get_provider()

    multicall = Multicall(w3, "fuji")
    multicall_write = MulticallWrite(w3, "fuji")
    targets = list(Asset.objects.all())
    approve_erc20_calls = []
    pangolin_liquidity_get_pair_reserve_calls = []
    pangolin_liquidity_management_calls = []
    ftx_prices = []
    pangolin_router = w3.eth.contract(
        addresses["pangolin"]["Router"], abi=PangolinRouter
    )
    # get pair
    # get balance
    multicall_address = "0xcA11bde05977b3631167028862bE2a173976CA11"
    for target in targets:

        target_asset = w3.eth.contract(
            address=to_canonical_address(target.address), abi=ERC20_ABI
        )
        approve_erc20_calls.append(
            multicall_write.create_call(
                target_asset,
                "approve",
                [multicall_address, int(1e30)],
            ),
        )
    print(approve_erc20_calls)
    result = multicall_write.call(approve_erc20_calls)


def approve_pangoli_router_to_use_all_asset_in_multicall_contract():
    """approve multicall contract to use all assets (in asset DB) of the user wallet"""
    w3 = get_provider()

    multicall = Multicall(w3, "fuji")
    multicall_write = MulticallWrite(w3, "fuji")
    targets = list(Asset.objects.all())
    approve_erc20_calls = []

    # get pair
    # get balance
    multicall_address = "0xcA11bde05977b3631167028862bE2a173976CA11"
    for target in targets:
        target_asset = w3.eth.contract(
            address=to_canonical_address(target.address), abi=ERC20_ABI
        )
        approve_erc20_calls.append(
            multicall_write.create_call(
                target_asset,
                "approve",
                [addresses["pangolin"]["Router"], int(1e30)],
            ),
        )
    multicall_write.call(approve_erc20_calls)


approve_pangoli_router_to_use_all_asset_in_multicall_contract()
