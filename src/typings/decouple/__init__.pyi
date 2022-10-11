"""
This type stub file was generated by pyright.
"""

import sys

"""Varint encoder/decoder

varints are a common encoding for variable length integer data, used in
libraries such as sqlite, protobuf, v8, and more.

Here's a quick and dirty module to help avoid reimplementing the same thing
over and over again.
"""
if sys.version > '3':
    ...
else:
    ...
def encode(number):
    """Pack `number` into varint bytes"""
    ...

def decode_stream(stream): # -> int:
    """Read a varint from `stream`"""
    ...

def decode_bytes(buf): # -> int:
    """Read a varint from from `buf` bytes"""
    ...
