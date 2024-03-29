"""
This type stub file was generated by pyright.
"""

import re
from eth_utils import ValidationError

IDENTIFIER_REGEX = ...
TYPE_REGEX = ...
def validate_has_attribute(attr_name, dict_data): # -> None:
    ...

def validate_types_attribute(structured_data): # -> None:
    ...

def validate_field_declared_only_once_in_struct(field_name, struct_data, struct_name): # -> None:
    ...

EIP712_DOMAIN_FIELDS = ...
def used_header_fields(EIP712Domain_data): # -> list:
    ...

def validate_EIP712Domain_schema(structured_data): # -> None:
    ...

def validate_primaryType_attribute(structured_data): # -> None:
    ...

def validate_structured_data(structured_data): # -> None:
    ...

