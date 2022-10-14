import json
from web3 import Web3
from django.core.management import BaseCommand

from django_ethereum_events.chainevents import AbstractEventReceiver
from django_ethereum_events.models import MonitoredEvent

from abi.ocf.FundDeployer import FundDeployer

from fund.models import Fund
from utils.multicall.multicall import Multicall
from utils.utils import get_provider


class NewFundCreatedReceiver(AbstractEventReceiver):
    def save(self, decoded_event):

        fund_data = json.loads(Web3.toJSON(decoded_event))
        w3 = get_provider()
        multicall = Multicall(w3, "fuji")

        fund = Fund(
            vault_proxy=fund_data["args"]["vaultProxy"],
            creator=fund_data["args"]["creator"],
            comptroller_proxy=fund_data["args"]["comptrollerProxy"],
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
