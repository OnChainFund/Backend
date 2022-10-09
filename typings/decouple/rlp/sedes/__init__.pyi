"""
This type stub file was generated by pyright.
"""

from rlp.exceptions import DeserializationError, SerializationError
from rlp.atomic import Atomic

class Text:
    """A sedes object for encoded text data of certain length.

    :param min_length: the minimal length in encoded characters or `None` for no lower limit
    :param max_length: the maximal length in encoded characters or `None` for no upper limit
    :param allow_empty: if true, empty strings are considered valid even if
                        a minimum length is required otherwise
    """
    def __init__(self, min_length=..., max_length=..., allow_empty=..., encoding=...) -> None:
        ...
    
    @classmethod
    def fixed_length(cls, l, allow_empty=...): # -> Self@Text:
        """Create a sedes for text data with exactly `l` encoded characters."""
        ...
    
    @classmethod
    def is_valid_type(cls, obj): # -> bool:
        ...
    
    def is_valid_length(self, l): # -> bool:
        ...
    
    def serialize(self, obj):
        ...
    
    def deserialize(self, serial):
        ...
    


text = ...
