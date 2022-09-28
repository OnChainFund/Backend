import json
import string

from web3 import Web3
from web3.middleware import geth_poa_middleware
from web3.gas_strategies.time_based import fast_gas_price_strategy
from django.conf import settings


def get_provider() -> Web3.HTTPProvider:
    w3 = Web3(Web3.HTTPProvider(settings.ETHEREUM_NODE_URI))
    #w3.eth.set_gas_price_strategy(fast_gas_price_strategy)
    w3.middleware_onion.inject(geth_poa_middleware, layer=0)
    return w3


def read_json_file(filename: string) -> list:
    with open("deployment/" + filename + ".json") as json_file:
        data = json.load(json_file)
        return data


def args_to_string(args: list) -> str:
    result = ""
    for arg in args:
        if type(arg) == str:
            result += "'" + arg + "'"
            result += ","
        elif type(arg) == int:
            result += str(arg)
            result += ","
        elif type(arg) == bool:
            result += str(arg)
            result += ","
    result_remove_last = result[:-1]
    return result_remove_last
