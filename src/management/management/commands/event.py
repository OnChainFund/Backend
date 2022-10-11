# import the following dependencies
import json
from web3 import Web3
import asyncio
from abi.ocf.FundDeployer import FundDeployer
from fund.models import Fund
from asgiref.sync import sync_to_async

# add blockchain connection information
infura_url = "https://api.avax-test.network/ext/bc/C/rpc"
web3 = Web3(Web3.HTTPProvider(infura_url))

fund_deployer_address = "0xd590Dc2e92ce061d941A7362F9DD92540679Ef8f"


contract = web3.eth.contract(address=fund_deployer_address, abi=FundDeployer)


# define function to handle events and print to the console
@sync_to_async
def handle_event(event):
    print(event)
    print(Web3.toJSON(event))
    fund_data = json.loads(Web3.toJSON(event))
    print(fund_data["args"])

    fund = Fund(
        vault_proxy=fund_data["args"]["vaultProxy"],
        creator=fund_data["args"]["creator"],
        comptroller_proxy=fund_data["args"]["comptrollerProxy"],
    )
    (fund.save())


# asynchronous defined function to loop
# this loop sets up an event filter and is looking for new entires for the "NewFundCreated" event
# this loop runs on a poll interval
async def log_loop(event_filter, poll_interval):
    while True:
        for NewFundCreated in event_filter.get_new_entries():
            await handle_event(NewFundCreated)
        await asyncio.sleep(poll_interval)


# when main is called
# create a filter for the latest block and look for the "NewFundCreated" event for the contract
# run an async loop
# try to run the log_loop function above every 2 seconds
def listen_to_event():
    event_filter = contract.events.NewFundCreated.createFilter(fromBlock="latest")
    # block_filter = web3.eth.filter('latest')
    # tx_filter = web3.eth.filter('pending')
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(asyncio.gather(log_loop(event_filter, 2)))
    finally:
        loop.close()