from email.headerregistry import Address
from pkg_resources import get_provider
from try_app.multicall import Multicall
from utils.utils import get_provider
from abi.others.ERC20 import ERC20 as ERC20_ABI

w3 = get_provider()
multicall = Multicall(w3, "fuji")
USDT = w3.eth.contract(
    address="0xd1Cc87496aF84105699E82D46B6c5Ab6775Afae4", abi=ERC20_ABI
)
calls = [
    multicall.create_call(
        USDT,
        "balanceOf",
        ["0x9dd3b3471AF147DF6c7E93ff35a5f04eE9342e9C"],
    ),
    multicall.create_call(
        USDT,
        "balanceOf",
        ["0xA3579C4c2057b58244DBc7DF5411C79d5F63a8A7"],
    ),
    multicall.create_call(
        USDT,
        "balanceOf",
        [
            "0xA3579C4c2057b58244DBc7DF5411C79d5F63a8A7",
        ],
    ),
]

result = multicall.call(calls)
print(result)
print("USDT: ", int(result[1][0].hex(), 16) / 10**6)
print("USDT: ", int(result[1][1].hex(), 16) / 10**6)
