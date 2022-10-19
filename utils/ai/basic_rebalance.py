from web3.contract import Contract

from abi.ocf.ComptrollerLib import ComptrollerLib
from utils.ai.get_weights import get_weights_with_asset_address
from utils.multicall.multicall_write import MulticallWrite
from utils.utils import get_provider
from utils.web3.pangolin_integration.utils import get_call_args

fund_address = "0xdB15F01C3C7Dd083e0434Dd09E740ca3906Ab41c"


w3 = get_provider()

multicall_write = MulticallWrite(w3, "fuji")
GAV = 909910
Buffer = 0.1
usdt = "0xd1Cc87496aF84105699E82D46B6c5Ab6775Afae4"
rebalance_calls = []
comptroller_proxy: Contract = w3.eth.contract(  # type: ignore
    # fund.comptroller_proxy, abi=ComptrollerLib  # type: ignore
    "0x7B3cED82De54424EbC9aFbBcD6513B9aCe1A002D",  # type: ignore
    abi=ComptrollerLib,  # type: ignore
)
for key, value in get_weights_with_asset_address().items():
    print(key, "->", int(GAV * (1 - Buffer) * value * 1e18))
    if not key == usdt:
        rebalance_calls.append(
            multicall_write.create_call(
                comptroller_proxy,
                "callOnExtension",
                [
                    "0xbf07f33165Cc5d64c299E4567e19575AabB80575",
                    0,
                    get_call_args(
                        from_asset=usdt,
                        to_asset=key,
                        outgoing_asset_amount=int(GAV * (1 - Buffer) * value * 1e18),
                        min_incoming_asset_amount=int(1e3),
                    ),
                ],
            ),
        )
result = multicall_write.call(rebalance_calls)
