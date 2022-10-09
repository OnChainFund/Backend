# pyright: strict

from eth_hash import Keccak256
from pkg_resources import get_provider
from contract.contracts.deployment.ocf.ComptrollerLib import ComptrollerLib
from contract.contracts.deployment.others.Addresses import Addresses
from try_app.multicall_write import Multicall
from utils.utils import get_provider
from fund.models import Fund
from typing import List, Set, Dict, Tuple, Optional
from decouple import config

# from eth_abi import encode, encode_abi
import eth_abi
print(ComptrollerLib)
pangolin_exchange_adaptor = "0x9c734a1af86273c0712a83ac154c51f8f5b21762"
from_asset: str = Addresses["WAVAX"]
to_asset: str = Addresses["USDT"]


def encode_args(types: List[str], args: list[str]):
    hex = eth_abi.encode(types, args)
    return hex


def call_on_integration_args(adapter: str, encodedCallArgs: bytes, selector: bytes):
    return encode_args(
        ["address", "bytes4", "bytes"], [adapter, selector, encodedCallArgs]
    )


def pangolin_take_prder_args(
    min_incoming_asset_amount: float, outgoing_asset_amount: float, path: List[str]
):
    return encode_args(
        ["address[]", "uint256", "uint256"],
        [path, int(outgoing_asset_amount), int(min_incoming_asset_amount)],
    )


take_order_args = pangolin_take_prder_args(
    min_incoming_asset_amount=1,
    outgoing_asset_amount=1e5,
    path=[from_asset, to_asset],
)
call_args = call_on_integration_args(
    # pangolin_exchange_adaptor,
    "0x5A6453C51B49e22A191eFb504FeD192754A6F619",
    take_order_args,
    b"0x03e38a2b",
)
# print(Keccak256("takeOrder(address,bytes,bytes)"))

w3 = get_provider()
multicall = Multicall(w3, "fuji")
fund = Fund.objects.first()
comptroller_proxy = w3.eth.contract(fund.comptroller_proxy, abi=ComptrollerLib)
print(call_args)
# calls = [
#   multicall.create_call(
#       comptroller_proxy,
#       "callOnExtension",
#       [
#           "0xbf07f33165Cc5d64c299E4567e19575AabB80575",
#           0,
#           call_args,
#       ],
#   ),
# ]#
# result = multicall.call(calls)

# txn = comptroller_proxy.functions.callOnExtension(
#    "0xbf07f33165Cc5d64c299E4567e19575AabB80575", 0, call_args
# ).buildTransaction(
#    {
#        "chainId": 43113,
#        "gas": 7900000,
#        # "maxFeePerGas": w3.toWei("30", "gwei"),
#        # "maxPriorityFeePerGas": w3.toWei("1", "gwei"),
#        "nonce": w3.eth.getTransactionCount(Addresses["user_1"]),
#    }
# )
# signed_txn = w3.eth.account.sign_transaction(txn, private_key=config("PRIVATE_KEY"))
# w3.eth.sendRawTransaction(signed_txn.rawTransaction)
#
