from pprint import pprint
from utils import read_json_file, get_provider
from decouple import config
from pprint import pprint

private_key = config('PRIVATE_KEY')
w3 = get_provider()
#pprint(w3.middleware_onion.middlewares)

# 自動簽名
from web3.middleware import construct_sign_and_send_raw_middleware
from eth_account import Account
#acct = Account.from_key(private_key)

acct = Account.from_key(private_key)
w3.middleware_onion.add(construct_sign_and_send_raw_middleware(acct))
w3.eth.default_account = acct
#pprint(dir(acct))
#print(w3.eth.get_balance(acct.address))
dynamic_fee_transaction = {
    'type': '0x2',  # optional - defaults to '0x2' when dynamic fee transaction params are present
    'from': acct.address,  # optional if w3.eth.default_account was set with acct.address
    'to': "0x9Cd4b8a8709cb598bF1d248f20aeD3E50ce9f81a",
    'value': 22,
    'maxFeePerGas': 30000000000,  # required for dynamic fee transactions
    'maxPriorityFeePerGas': 1000000000,  # required for dynamic fee transactions
}
w3.eth.send_transaction(dynamic_fee_transaction)
#pprint(w3.middleware_onion.middlewares)

## send transaction
#addresses = (read_json_file('others/Addresses'))
#wavax_abi = (read_json_file('others/WAVAX'))
#contract = w3.eth.contract(addresses["WAVAX"], abi=wavax_abi)
#txn = contract.functions.transfer(addresses["user_2"], 100).transact()
#w3.eth.send_transaction(txn)