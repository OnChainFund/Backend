import rlp
from eth_typing import HexStr
from eth_utils import to_bytes
from ethereum.transactions import Transaction

def hex_to_bytes(data: str) -> bytes:
    return to_bytes(hexstr=HexStr(data))