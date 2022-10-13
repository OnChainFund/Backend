from decimal import Decimal
from web3.datastructures import AttributeDict
from utils.multicall.multicall import Call
from management.web3.multicall_custome import MulticallCustom as Multicall
from fund.models import Asset
from utils.utils import get_provider

w3 = get_provider()
# 取得所有 token
# 取得要計算 balance 的物件
def from_wei(value):
    return value / 1e18


def generate_multicall(call_list: list):
    multi = Multicall(call_list, _w3=w3)
    return multi


fund_vault_proxy_address = "0x9dd3b3471AF147DF6c7E93ff35a5f04eE9342e9C"

VAULT_PROXY = "0x9dd3b3471AF147DF6c7E93ff35a5f04eE9342e9C"
multi = Multicall(
    [
        Call(
            "0x6cEeB8fec16F7276F57ACF70C14ecA6008d3DDD4",
            ["balanceOf(address)(uint256)", VAULT_PROXY],
            _w3=w3,
        ),
        Call(
            "0x6cEeB8fec16F7276F57ACF70C14ecA6008d3DDD4",
            ["balanceOf(address)(uint256)", VAULT_PROXY],
            _w3=w3,
        ),
    ],
    _w3=w3,
)
multi()
# data = Call(
#    "0x6cEeB8fec16F7276F57ACF70C14ecA6008d3DDD4",
#    ["balanceOf(address)(uint256)", VAULT_PROXY],
#    [["fish", from_wei]],
#    _w3=w3,
# )()


data = Call(
    "0x6cEeB8fec16F7276F57ACF70C14ecA6008d3DDD4",
    ["balanceOf(address)(uint256)", VAULT_PROXY],
    _w3=w3,
)()
print(data)
# print(data())
