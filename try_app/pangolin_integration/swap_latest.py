# pyright: strict

from eth_hash import Keccak256
from pkg_resources import get_provider
from contract.contracts.deployment.ocf.ComptrollerLib import ComptrollerLib
from contract.contracts.deployment.others.Addresses import Addresses
from try_app.multicall_write import Multicall
from utils.utils import get_provider
from fund.models import Fund
from decouple import config
from eth_abi import is_encodable

# print(ComptrollerLib)
my_bytes = "0x03".encode()
print("0x03e38a2b")
print("0x03e38a2b".encode())
print(type(my_bytes))

print(len(my_bytes))
print(is_encodable("bytes4", my_bytes))
