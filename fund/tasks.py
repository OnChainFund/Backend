from utils.utils import get_provider
from contract.contracts.deployment.others.FundValueCalculator import FundValueCalculator
from contract.contracts.deployment.others.Addresses import Addresses
from .models import Price


def get_price(vault_proxy: str, quote_asset: str):
    w3 = get_provider()
    fund_value_calculator_contract = w3.eth.contract(
        Addresses["ocf"]["FundValueCalculator"],
        abi=FundValueCalculator,
    )
    data = fund_value_calculator_contract.encodeABI(
        fn_name="calcGavInAsset",
        args=[vault_proxy, quote_asset],
    )
    tx = w3.eth.call(
        {
            "value": 0,
            "gas": 7900000,
            "maxFeePerGas": w3.toWei("30", "gwei"),
            "maxPriorityFeePerGas": 1000000000,
            "to": Addresses["ocf"]["FundValueCalculator"],
            "data": data,
        }
    )

    return int(tx.hex()[2:], 16) / 1e18


def add_price_to_fund():
    # get price
    # write price in model
    pass


print(
    get_price(
        "0x02b7a6d41F929a2d09D6dd8aF5537c1d1fe2E678",
        Addresses["USDT"],
    )
)
