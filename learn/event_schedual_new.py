# import the following dependencies
import time
import json
from web3 import Web3
import asyncio

from fund_deployer_abi import FUND_DEPLOYER_ABI

# add your blockchain connection information
infura_url = "https://api.avax-test.network/ext/bc/C/rpc"
web3 = Web3(Web3.HTTPProvider(infura_url))

fund_deployer_address = "0xd590Dc2e92ce061d941A7362F9DD92540679Ef8f"


contract = web3.eth.contract(address=fund_deployer_address, abi=FUND_DEPLOYER_ABI)


def handle_event(event):
    print(Web3.toJSON(event))


event_filter = contract.events.NewFundCreated.createFilter(fromBlock=14525546)
print(event_filter.get_new_entries())
for PairCreated in event_filter.get_new_entries():
    handle_event(PairCreated)
    print(PairCreated)
