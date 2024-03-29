"""
This type stub file was generated by pyright.
"""

import operator
import random
import sys
from typing import Any, Callable, List, NoReturn, Optional, TYPE_CHECKING, Tuple, Type
from eth_tester.exceptions import BlockNotFound, FilterNotFound, TransactionNotFound, ValidationError
from eth_typing import HexAddress, HexStr
from eth_utils import decode_hex, encode_hex, is_null, keccak
from eth_utils.curried import apply_formatter_if
from eth_utils.toolz import compose, curry, excepts
from web3.types import LogReceipt, RPCResponse, TParams, TReturn, TValue, TxReceipt
from eth_tester import EthereumTester

if TYPE_CHECKING:
    ...
def not_implemented(*args: Any, **kwargs: Any) -> NoReturn:
    ...

@curry
def call_eth_tester(fn_name: str, eth_tester: EthereumTester, fn_args: Any, fn_kwargs: Optional[Any] = ...) -> RPCResponse:
    ...

def without_eth_tester(fn: Callable[[TParams], TReturn]) -> Callable[[EthereumTester, TParams], TReturn]:
    ...

def without_params(fn: Callable[[TParams], TReturn]) -> Callable[[EthereumTester, TParams], TReturn]:
    ...

@curry
def preprocess_params(eth_tester: EthereumTester, params: Any, preprocessor_fn: Callable[..., Any]) -> Tuple[EthereumTester, Callable[..., Any]]:
    ...

def static_return(value: TValue) -> Callable[..., TValue]:
    ...

def client_version(eth_tester: EthereumTester, params: Any) -> str:
    ...

@curry
def null_if_excepts(exc_type: Type[BaseException], fn: Callable[..., TReturn]) -> Callable[..., TReturn]:
    ...

null_if_block_not_found = ...
null_if_transaction_not_found = ...
null_if_filter_not_found = ...
null_if_indexerror = ...
@null_if_indexerror
@null_if_block_not_found
def get_transaction_by_block_hash_and_index(eth_tester: EthereumTester, params: Any) -> TxReceipt:
    ...

@null_if_indexerror
@null_if_block_not_found
def get_transaction_by_block_number_and_index(eth_tester: EthereumTester, params: Any) -> TxReceipt:
    ...

def create_log_filter(eth_tester: EthereumTester, params: Any) -> int:
    ...

def get_logs(eth_tester: EthereumTester, params: Any) -> List[LogReceipt]:
    ...

@without_params
def create_new_account(eth_tester: EthereumTester) -> HexAddress:
    ...

def personal_send_transaction(eth_tester: EthereumTester, params: Any) -> HexStr:
    ...

API_ENDPOINTS = ...
