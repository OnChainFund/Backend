"""
This type stub file was generated by pyright.
"""

from functools import lru_cache
from hashlib import sha256
from typing import Mapping, Union

'''Base58 encoding

Implementations of Base58 and Base58Check encodings that are compatible
with the bitcoin network.
'''
__version__ = ...
BITCOIN_ALPHABET = ...
RIPPLE_ALPHABET = ...
XRP_ALPHABET = ...
alphabet = ...
def scrub_input(v: Union[str, bytes]) -> bytes:
    ...

def b58encode_int(i: int, default_one: bool = ..., alphabet: bytes = ...) -> bytes:
    """
    Encode an integer using Base58
    """
    ...

def b58encode(v: Union[str, bytes], alphabet: bytes = ...) -> bytes:
    """
    Encode a string using Base58
    """
    ...

def b58decode_int(v: Union[str, bytes], alphabet: bytes = ..., *, autofix: bool = ...) -> int:
    """
    Decode a Base58 encoded string as an integer
    """
    ...

def b58decode(v: Union[str, bytes], alphabet: bytes = ..., *, autofix: bool = ...) -> bytes:
    """
    Decode a Base58 encoded string
    """
    ...

def b58encode_check(v: Union[str, bytes], alphabet: bytes = ...) -> bytes:
    """
    Encode a string using Base58 with a 4 character checksum
    """
    ...

def b58decode_check(v: Union[str, bytes], alphabet: bytes = ..., *, autofix: bool = ...) -> bytes:
    '''Decode and verify the checksum of a Base58 encoded string'''
    ...
