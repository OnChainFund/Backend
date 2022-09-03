from utils import read_json_file, get_provider
from decouple import config

private_key = config('PRIVATE_KEY')
w3 = get_provider()
wavax_abi = (read_json_file('others/WAVAX'))
addresses = (read_json_file('others/Addresses'))
funds = (read_json_file('others/Funds'))
contract = w3.eth.contract(addresses["WAVAX"], abi=wavax_abi)
# basic info
print(contract.functions.name().call())
print(contract.functions.totalSupply().call())
# check balance
print(contract.functions.balanceOf(addresses["user_1"]).call())
print(contract.functions.balanceOf(funds["T2"]["vaultProxy"]).call())

# transfer token
txn = contract.functions.transfer(addresses["user_2"], 100)
print(dir(txn))
#｀txn.transact({'from': addresses["user_1"]})


txn = contract.functions.transfer(addresses["user_2"], 100).build_transaction({
     'chainId': 43113,
     'gas': 7900000,
     'maxFeePerGas': w3.toWei('30', 'gwei'),
     'maxPriorityFeePerGas': w3.toWei('1', 'gwei'),
     'nonce': w3.eth.getTransactionCount(addresses["user_1"]),
 })
signed_txn = w3.eth.account.sign_transaction(txn, private_key=private_key)
print(signed_txn.rawTransaction)
print(dir(signed_txn))
w3.eth.sendRawTransaction(signed_txn.rawTransaction) 
#w3.eth.sendTransaction(signed_txn)