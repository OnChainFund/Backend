# import the following dependencies
import json
from web3 import Web3
import asyncio
from abi.ocf.FundDeployer import FundDeployer
from fund.models import Fund
from asgiref.sync import sync_to_async
from threading import Thread
import time

infura_url = "https://api.avax-test.network/ext/bc/C/rpc"
web3 = Web3(Web3.HTTPProvider(infura_url))

fund_deployer_address = "0xd590Dc2e92ce061d941A7362F9DD92540679Ef8f"


contract = web3.eth.contract(address=fund_deployer_address, abi=FundDeployer)


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


async def log_loop(event_filter, poll_interval):
    while True:
        for event in event_filter.get_new_entries():
            handle_event(event)
        time.sleep(poll_interval)


def listen_to_event():
    event_filter = contract.events.NewFundCreated.createFilter(fromBlock="latest")
    worker = Thread(target=log_loop, args=(event_filter, 5), daemon=True)
    worker.start()
