"""
This type stub file was generated by pyright.
"""

from typing import Any, Dict, Sequence
from toolz import assoc, dissoc
from eth_account._utils.validation import is_rlp_structured_access_list, is_rpc_structured_access_list

def set_transaction_type_if_needed(transaction_dict: Dict[str, Any]) -> Dict[str, Any]:
    ...

def transaction_rpc_to_rlp_structure(dictionary: Dict[str, Any]) -> Dict[str, Any]:
    """
    Convert a JSON-RPC-structured transaction to an rlp-structured transaction.
    """
    ...

def transaction_rlp_to_rpc_structure(dictionary: Dict[str, Any]) -> Dict[str, Any]:
    """
    Convert an rlp-structured transaction to a JSON-RPC-structured transaction.
    """
    ...

