import json
from web3 import Web3
from django.core.management import BaseCommand

from django_ethereum_events.chainevents import AbstractEventReceiver
from django_ethereum_events.models import MonitoredEvent
from web3.contract import Contract
from abi.ocf.ComptrollerLib import ComptrollerLib
from eth_abi.abi import decode
from abi.ocf.FundDeployer import FundDeployer
from eth_utils.address import to_canonical_address
from abi.ocf.VaultLib import VaultLib
from fund.models import Fund, Wallet
from utils.multicall.multicall import Multicall
from utils.utils import get_provider
from abi.others.ERC20 import ERC20 as ERC20_ABI


class NewFundCreatedReceiver(AbstractEventReceiver):
    def save(self, decoded_event):
        data = json.loads(Web3.toJSON(decoded_event))
        # print(data)
        w3 = get_provider()
        multicall = Multicall(w3, "fuji")
        vault = w3.eth.contract(
            to_canonical_address(data["args"]["vaultProxy"]),
            abi=VaultLib,
        )
        comptroller = w3.eth.contract(
            to_canonical_address(data["args"]["comptrollerProxy"]),
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
            vault_proxy=data["args"]["vaultProxy"],
            creator=data["args"]["creator"],
            comptroller_proxy=data["args"]["comptrollerProxy"],
            symbol=str(decode(["string"], result[1][0])[0]),
            name=str(decode(["string"], result[1][1])[0]),
            denominated_asset=str(decode(["address"], result[1][2])[0]),
        )
        fund.save()
        # watch depositers
        MonitoredEvent.objects.register_event(
            event_name="SharesBought",
            contract_address=data["args"]["comptrollerProxy"],
            contract_abi=ComptrollerLib,
            event_receiver="management.management.receivers.SharesBoughtReceiver",
        )
        MonitoredEvent.objects.register_event(
            event_name="SharesRedeemed",
            contract_address=data["args"]["comptrollerProxy"],
            contract_abi=ComptrollerLib,
            event_receiver="management.management.receivers.SharesRedeemedReceiver",
        )

        # create wallet
        wallet_exist_or_create(data["args"]["creator"])


class SharesBoughtReceiver(AbstractEventReceiver):
    def save(self, decoded_event):
        data = json.loads(Web3.toJSON(decoded_event))
        print(data)
        wallet = wallet_exist_or_create(data["args"]["buyer"])
        if Fund.objects.filter(comptroller_proxy=data["address"]).exists():
            wallet.invested_funds.add(
                Fund.objects.filter(comptroller_proxy=data["address"]).get()
            )
            # check if the wallet is add to db
            pass


class SharesRedeemedReceiver(AbstractEventReceiver):
    def save(self, decoded_event):
        data = json.loads(Web3.toJSON(decoded_event))
        # check if the fund balance of the wallet is equal to zero
        if Fund.objects.filter(comptroller_proxy=data["address"]).exists():
            fund_object = Fund.objects.filter(comptroller_proxy=data["address"]).get()
            w3 = get_provider()
            fund_contract: Contract = w3.eth.contract(
                address=to_canonical_address(fund_object.vault_proxy), abi=ERC20_ABI
            )
            balance = fund_contract.functions.balanceOf(data["args"]["redeemer"]).call()
            if balance / 1e18 <= 0.01:
                wallet = wallet_exist_or_create(data["args"]["redeemer"])
                wallet.invested_funds.remove(fund_object)


def wallet_exist_or_create(address: str) -> Wallet:
    if Wallet.objects.filter(pk=address).exists():
        wallet = Wallet.objects.get(pk=address)
    else:
        wallet = Wallet(address=address)
        wallet.save()
    return wallet
