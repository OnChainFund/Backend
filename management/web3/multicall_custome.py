import asyncio
from time import time
from typing import Any, Dict, List, Optional, Tuple, Union

import aiohttp
import requests
from web3 import Web3

from multicall import Call
from multicall.constants import (
    GAS_LIMIT,
    MULTICALL2_ADDRESSES,
    MULTICALL2_BYTECODE,
    MULTICALL_ADDRESSES,
    w3,
)
from multicall.loggers import setup_logger
from multicall.utils import (
    await_awaitable,
    chain_id,
    gather,
    run_in_subprocess,
    state_override_supported,
)
from multicall.multicall import (
    NotSoBrightBatcher,
    _raise_or_proceed,
    batcher,
    unpack_batch_results,
    get_args,
    unpack_aggregate_outputs,
    CallResponse,
    logger,
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
            multicall_map = (
                MULTICALL_ADDRESSES
                if self.chainid in MULTICALL_ADDRESSES
                else MULTICALL2_ADDRESSES
            )
            self.multicall_sig = "aggregate((address,bytes)[])(uint256,bytes[])"
        else:
            multicall_map = MULTICALL2_ADDRESSES
            self.multicall_sig = "tryBlockAndAggregate(bool,(address,bytes)[])(uint256,uint256,(bool,bytes)[])"
        # self.multicall_address = multicall_map[self.chainid]
        self.multicall_address = "0xca11bde05977b3631167028862be2a173976ca11"

    