from decouple import config  # type: ignore
from eth_abi.abi import encode, encode_abi  # type: ignore
from eth_utils.hexadecimal import decode_hex
from web3.contract import Contract

from abi.ocf.ComptrollerLib import ComptrollerLib
from fund.models import Fund
from utils.constants.addresses import addresses
from utils.multicall.multicall_write import MulticallWrite
from utils.utils import get_provider


def encode_args(types: list[str], args: list[str | list[str] | int | bytes]):
    hex: bytes = encode(types, args)
    return hex


def call_on_integration_args(adapter: str, encodedCallArgs: bytes, selector: bytes):
    return encode_args(
        ["address", "bytes4", "bytes"], [adapter, selector, encodedCallArgs]
    )


def pangolin_take_order_args(
    min_incoming_asset_amount: int, outgoing_asset_amount: int, path: list[str]
):
    return encode_args(
        ["address[]", "uint256", "uint256"],
        [path, int(outgoing_asset_amount), int(min_incoming_asset_amount)],
    )


def get_call_args(
    from_asset: str,
    to_asset: str,
    outgoing_asset_amount: int,
    min_incoming_asset_amount: int,
):
    take_order_args = pangolin_take_order_args(
        min_incoming_asset_amount=min_incoming_asset_amount,
        outgoing_asset_amount=outgoing_asset_amount,
        path=[from_asset, to_asset],
    )
    call_args = call_on_integration_args(
        # pangolin_exchange_adaptor,
        "0x5A6453C51B49e22A191eFb504FeD192754A6F619",
        decode_hex(take_order_args.hex()),
        decode_hex("0x03e38a2b"),
    )
    return call_args
