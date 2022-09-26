from typing import List, Optional

from web3 import Web3

from utils.multicall import Call
from utils.multicall.constants import (
    GAS_LIMIT,
    w3,
)
from utils.multicall.utils import (
    chain_id,
)
from utils.multicall.multicall import (
    Multicall,
)


class MulticallCustom(Multicall):
    def __init__(
        self,
        calls: List[Call],
        block_id: Optional[int] = None,
        require_success: bool = True,
        gas_limit: int = GAS_LIMIT,
        _w3: Web3 = w3,
    ) -> None:
        self.calls = calls
        self.block_id = block_id
        self.require_success = require_success
        self.gas_limit = gas_limit
        self.w3 = _w3
        self.chainid = chain_id(self.w3)
        if require_success is True:
            self.multicall_sig = "tryBlockAndAggregate(bool,(address,bytes)[])(uint256,uint256,(bool,bytes)[])"
        # self.multicall_address = multicall_map[self.chainid]
        self.multicall_address = "0xca11bde05977b3631167028862be2a173976ca11"
