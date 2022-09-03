from pprint import pprint
from utils import read_json_file, get_provider
from web3 import Web3
w3 = get_provider()
transaction = w3.eth.get_transaction("0x81daafa458be5a59731411e5f374ff0ff9940a0e452a9512447e01f912389248")
#print(transaction)
fund_deployer_data = (read_json_file('enzyme/FundDeployer'))
contract = w3.eth.contract(fund_deployer_data["address"], abi=fund_deployer_data["abi"])
input_data = contract.decode_function_input(transaction.input)
#print(input_data)
#print(dir(transaction))
"""['__abstractmethods__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__module__', '__ne__', '__new__', '__orig_bases__', '__parameters__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__setattr__', '__sizeof__', '__slots__', '__str__', '__subclasshook__', '__weakref__', '_abc_impl', '_apply_if_mapping', '_is_protocol', '_repr_pretty_', 'accessList', 'blockHash', 'blockNumber', 'chainId', 'from', 'gas', 'gasPrice', 'get', 'hash', 'input', 'items', 'keys', 'maxFeePerGas', 'maxPriorityFeePerGas', 'nonce', 'r', 'recursive', 's', 'to', 'transactionIndex', 'type', 'v', 'value', 'values']"""
print((transaction.accessList))
