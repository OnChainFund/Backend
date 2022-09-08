import json
import string

from web3 import Web3
from web3.middleware import geth_poa_middleware


def get_provider() -> Web3.HTTPProvider:
    w3 = Web3(Web3.HTTPProvider("https://api.avax-test.network/ext/bc/C/rpc"))
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
    result_remove_last = result[:-1]
    return result_remove_last
