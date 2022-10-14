import json
from web3 import Web3
from django.core.management import BaseCommand

from django_ethereum_events.chainevents import AbstractEventReceiver
from django_ethereum_events.models import MonitoredEvent
from abi.ocf.ComptrollerLib import ComptrollerLib
from eth_abi.abi import decode
from abi.ocf.FundDeployer import FundDeployer
from eth_utils.address import to_canonical_address
from abi.ocf.VaultLib import VaultLib
from fund.models import Fund
from utils.multicall.multicall import Multicall
from utils.utils import get_provider


class NewFundCreatedReceiver(AbstractEventReceiver):
    def save(self, decoded_event):

        fund_data = json.loads(Web3.toJSON(decoded_event))
        print(fund_data)
        w3 = get_provider()
        multicall = Multicall(w3, "fuji")
        vault = w3.eth.contract(
            to_canonical_address(fund_data["args"]["vaultProxy"]),
            abi=VaultLib,
        )
        comptroller = w3.eth.contract(
            to_canonical_address(fund_data["args"]["comptrollerProxy"]),
            abi=ComptrollerLib,
        )
        calls = [
            multicall.create_call(
                vault,
                "symbol",
                [],
            ),
            multicall.create_call(
                vault,
                "name",
                [],
            ),
            multicall.create_call(
                comptroller,
                "getDenominationAsset",
                [],
            ),
        ]

        result = multicall.call(calls)

        fund = Fund(
            vault_proxy=fund_data["args"]["vaultProxy"],
            creator=fund_data["args"]["creator"],
            comptroller_proxy=fund_data["args"]["comptrollerProxy"],
            symbol=str(decode(["string"], result[1][0])[0]),
            name=str(decode(["string"], result[1][1])[0]),
            denominated_asset=str(decode(["address"], result[1][2])[0]),
        )
        fund.save()


class DepositReceiver(AbstractEventReceiver):
    def save(self, decoded_event):
        fund_data = json.loads(Web3.toJSON(decoded_event))

        fund = Fund(
            vault_proxy=fund_data["args"]["vaultProxy"],
            creator=fund_data["args"]["creator"],
            comptroller_proxy=fund_data["args"]["comptrollerProxy"],
        )
        fund.save()


class WithdrawReceiver(AbstractEventReceiver):
    def save(self, decoded_event):
        fund_data = json.loads(Web3.toJSON(decoded_event))

        fund = Fund(
            vault_proxy=fund_data["args"]["vaultProxy"],
            creator=fund_data["args"]["creator"],
            comptroller_proxy=fund_data["args"]["comptrollerProxy"],
        )
        fund.save()
