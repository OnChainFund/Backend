import json
from web3 import Web3
from django.core.management import BaseCommand

from django_ethereum_events.chainevents import AbstractEventReceiver
from django_ethereum_events.models import MonitoredEvent

from abi.ocf.FundDeployer import FundDeployer

from fund.models import Fund

fund_deployer_address = "0xd590Dc2e92ce061d941A7362F9DD92540679Ef8f"
fund_deployer_abi = FundDeployer


class TestReceiver(AbstractEventReceiver):
    def save(self, decoded_event):
        print("Received event: {}".format(decoded_event))
        fund_data = json.loads(Web3.toJSON(decoded_event))

        
        fund = Fund(
            vault_proxy=fund_data["args"]["vaultProxy"],
            creator=fund_data["args"]["creator"],
            comptroller_proxy=fund_data["args"]["comptrollerProxy"],
        )
        fund.save()


receiver = "management.management.commands.register_events.TestReceiver"

# List of ethereum events to monitor the blockchain for
DEFAULT_EVENTS = [
    ("NewFundCreated", fund_deployer_address, fund_deployer_abi, receiver),
]


class Command(BaseCommand):
    def handle(self, *args, **options):
        monitored_events = MonitoredEvent.objects.all()
        for event in DEFAULT_EVENTS:

            if not monitored_events.filter(
                name=event[0], contract_address__iexact=event[1]
            ).exists():
                self.stdout.write(
                    "Creating monitor for event {} at {}".format(event[0], event[1])
                )

                MonitoredEvent.objects.register_event(*event)

        self.stdout.write(self.style.SUCCESS("Events are up to date"))
