from django.db import models
from django.utils.translation import gettext_lazy as _

from web3 import Web3

from .validators import validate_checksumed_address


class EthereumAddressField(models.CharField):
    default_validators = [validate_checksumed_address]
    description = "Ethereum address"

    def __init__(self, *args, **kwargs):
        kwargs["max_length"] = 42
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        del kwargs["max_length"]
        return name, path, args, kwargs

    def from_db_value(self, value):
        return self.to_python(value)

    def to_python(self, value):
        value = super().to_python(value)
        if value:
            return Web3.isChecksumAddress(value)
        else:
            return value

    def get_prep_value(self, value):
        value = super().get_prep_value(value)
        if value:
            return Web3.isChecksumAddress(value)
        else:
            return value
