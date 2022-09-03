from web3 import Web3
from web3.middleware import geth_poa_middleware

w3 = Web3(Web3.HTTPProvider('https://api.avax-test.network/ext/bc/C/rpc'))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)

#print(w3.eth.get_block(12345))
print(w3.eth.get_balance('0x742d35Cc6634C0532925a3b844Bc454e4438f44e'))
print(w3.fromWei(3841357360894980500000001, 'ether'))
