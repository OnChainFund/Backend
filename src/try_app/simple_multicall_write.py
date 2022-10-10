from email.headerregistry import Address
from pkg_resources import get_provider
from contract.contracts.deployment.others.Addresses import Addresses
from contract.contracts.deployment.others.PangolinRouter import PangolinRouter
from try_app.multicall_write import Multicall
from utils.utils import get_provider
from contract.contracts.deployment.others.ERC20 import ERC20 as ERC20_ABI
from contract.contracts.deployment.others.chain_link.MockV3Aggregator import (
    MockV3Aggregator,
)

w3 = get_provider()
multicall = Multicall(w3, "fuji")
mock_v3_aggregator_address = "0x15fE0276686097996D6c4724762E8D1BF74E9471"
price = 75.04 * 1e8
mock_v3_aggregator = w3.eth.contract(
    mock_v3_aggregator_address,
    abi=MockV3Aggregator,
)
USDT = w3.eth.contract(
    address="0xd1Cc87496aF84105699E82D46B6c5Ab6775Afae4", abi=ERC20_ABI
)
pangolin_router = w3.eth.contract(Addresses["pangolin"]["Router"], abi=PangolinRouter)
calls = [
    multicall.create_call(
        pangolin_router,
        "swapExactTokensForTokens",
        [
            int(abs(1e5)),
            1,
            [
                "0xd1Cc87496aF84105699E82D46B6c5Ab6775Afae4",
                "0xbC9052c594261Acc1a26271567bDb72A8A1Acac9",
            ],
            Addresses["user_1"],
            1758392484,
        ],
    ),
]

result = multicall.call(calls)
print(result)
print((result.hex(), 16))
