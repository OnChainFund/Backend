from eth_abi import is_encodable
from eth_hash import Keccak256
from eth_abi.codec import ABICodec
from eth_abi.registry import registry as default_registry
from web3 import Web3
from sys import getsizeof

registry = default_registry.copy()
print("asdf")
encoded = str(Web3.keccak(text="takeOrder(address,bytes,bytes)"))
print(getsizeof(encoded))
print(getsizeof("0x03e38a2b"))
print(is_encodable('bytes4', b"0x03e38a2b"))
print(is_encodable('bytes8', b"0x03e38a2b"))
print(is_encodable('bytes32', b"0x03e38a2b"))
print(is_encodable('bytes16', b"0x03e38a2b"))
