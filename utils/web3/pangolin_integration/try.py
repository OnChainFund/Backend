from decouple import config  # type: ignore
from eth_abi.abi import encode, encode_abi
from eth_utils.hexadecimal import decode_hex
from pkg_resources import get_provider
from web3.contract import Contract

from abi.ocf.ComptrollerLib import ComptrollerLib
from fund.models import Fund
from utils.constants.addresses import addresses
from utils.multicall.multicall_write import MulticallWrite
from utils.utils import get_provider

pangolin_exchange_adaptor = "0x9c734a1af86273c0712a83ac154c51f8f5b21762"
from_asset: str = addresses["WAVAX"]  # type: ignore
to_asset: str = addresses["USDT"]  # type: ignore


def encode_args(types: list[str], args: list[str]):
    hex: bytes = encode(types, args)
    return hex


def call_on_integration_args(adapter: str, encodedCallArgs: bytes, selector: bytes):
    return encode_args(
        ["address", "bytes4", "bytes"], [adapter, selector, encodedCallArgs]
    )


def pangolin_take_order_args(
    min_incoming_asset_amount: float, outgoing_asset_amount: float, path: list[str]
):
    return encode_args(
        ["address[]", "uint256", "uint256"],
        [path, int(outgoing_asset_amount), int(min_incoming_asset_amount)],
    )


take_order_args = pangolin_take_order_args(
    min_incoming_asset_amount=1,
    outgoing_asset_amount=1e5,
    path=[from_asset, to_asset],
)

print(take_order_args)
print((take_order_args).hex())
call_args = call_on_integration_args(
    # pangolin_exchange_adaptor,
    "0x5A6453C51B49e22A191eFb504FeD192754A6F619",
    decode_hex(take_order_args.hex()),
    decode_hex("0x03e38a2b"),
)

w3 = get_provider()
multicall = MulticallWrite(w3, "fuji")
fund = Fund.objects.first()
comptroller_proxy: Contract = w3.eth.contract(
    fund.comptroller_proxy, abi=ComptrollerLib
)
calls = [
    multicall.create_call(
        comptroller_proxy,
        "callOnExtension",
        [
            "0xbf07f33165Cc5d64c299E4567e19575AabB80575",
            0,
            call_args,
        ],
    ),
]  #
result = multicall.call(calls)
