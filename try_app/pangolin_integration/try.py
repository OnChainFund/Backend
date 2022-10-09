from eth_abi import is_encodable
from eth_hash import Keccak256
from eth_abi.codec import ABICodec
from eth_abi.registry import registry as default_registry
from web3 import Web3
from sys import getsizeof

encoded = b"0x0000000000000000000000005a6453c51b49e22a191efb504fed192754a6f61903e38a2b00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000006000000000000000000000000000000000000000000000000000000000000000c000000000000000000000000000000000000000000000000000000000000000600000000000000000000000000000000000000000000000000000000005f5e100000000000000000000000000000000000000000000000000000000000000000100000000000000000000000000000000000000000000000000000000000000020000000000000000000000006ceeb8fec16f7276f57acf70c14eca6008d3ddd4000000000000000000000000d1cc87496af84105699e82d46b6c5ab6775afae4"

from eth_abi import decode

decode(
    ["address", "bytes4", "bytes"],
    encoded,
)
