"""
This type stub file was generated by pyright.
"""

from types import ModuleType
from typing import Any, Dict, Optional, Tuple, Union, overload

Buffer = Union[bytes, bytearray, memoryview]
class OcbMode:
    block_size: int
    nonce: Buffer
    def __init__(self, factory: ModuleType, nonce: Buffer, mac_len: int, cipher_params: Dict) -> None:
        ...
    
    def update(self, assoc_data: Buffer) -> OcbMode:
        ...
    
    @overload
    def encrypt(self, plaintext: Buffer) -> bytes:
        ...
    
    @overload
    def encrypt(self, plaintext: Buffer, output: Union[bytearray, memoryview]) -> None:
        ...
    
    @overload
    def decrypt(self, plaintext: Buffer) -> bytes:
        ...
    
    @overload
    def decrypt(self, plaintext: Buffer, output: Union[bytearray, memoryview]) -> None:
        ...
    
    def digest(self) -> bytes:
        ...
    
    def hexdigest(self) -> str:
        ...
    
    def verify(self, received_mac_tag: Buffer) -> None:
        ...
    
    def hexverify(self, hex_mac_tag: str) -> None:
        ...
    
    def encrypt_and_digest(self, plaintext: Buffer) -> Tuple[bytes, bytes]:
        ...
    
    def decrypt_and_verify(self, ciphertext: Buffer, received_mac_tag: Buffer) -> bytes:
        ...
    


