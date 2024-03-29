from utils.utils import get_provider
from abi.others.FundValueCalculator import FundValueCalculator
from fund.models import Fund, FundPrice
from utils.constants.addresses import addresses


def get_value(vault_proxy: str, quote_asset: str = addresses["USDT"]):
    w3 = get_provider()
    fund_value_calculator_contract = w3.eth.contract(
        addresses["ocf"]["FundValueCalculator"],
        abi=FundValueCalculator,
    )
    gav_data = fund_value_calculator_contract.encodeABI(
        fn_name="calcGavInAsset",
        args=[vault_proxy, quote_asset],
    )
    nav_per_share_data = fund_value_calculator_contract.encodeABI(
        fn_name="calcNetShareValueInAsset",
        args=[vault_proxy, quote_asset],
    )
    tx_gav = w3.eth.call(
        {
            "to": addresses["ocf"]["FundValueCalculator"],
            "data": gav_data,
        }
    )
    tx_nav = w3.eth.call(
        {
            "to": addresses["ocf"]["FundValueCalculator"],
            "data": nav_per_share_data,
        }
    )
    return [(int(tx_gav.hex()[2:], 16) / 1e18), (int(tx_nav.hex()[2:], 16) / 1e18)]


def get_fund_nav_per_share(vault_proxy: str, quote_asset: str = addresses["USDT"]):
    w3 = get_provider()
    fund_value_calculator_contract = w3.eth.contract(
        addresses["ocf"]["FundValueCalculator"],
        abi=FundValueCalculator,
    )

    nav_per_share_data = fund_value_calculator_contract.encodeABI(
        fn_name="calcNetShareValueInAsset",
        args=[vault_proxy, quote_asset],
    )

    tx_nav = w3.eth.call(
        {
            "to": addresses["ocf"]["FundValueCalculator"],
            "data": nav_per_share_data,
        }
    )
    return int(tx_nav.hex()[2:], 16) / 1e18


def get_fund_gav(vault_proxy: str, quote_asset: str = addresses["USDT"]):
    w3 = get_provider()
    fund_value_calculator_contract = w3.eth.contract(
        addresses["ocf"]["FundValueCalculator"],
        abi=FundValueCalculator,
    )
    gav_data = fund_value_calculator_contract.encodeABI(
        fn_name="calcGavInAsset",
        args=[vault_proxy, quote_asset],
    )
    tx_gav = w3.eth.call(
        {
            "to": addresses["ocf"]["FundValueCalculator"],
            "data": gav_data,
        }
    )
    return int(tx_gav.hex()[2:], 16) / 1e18


def add_price_to_fund(vault_proxy: str):
    # get price
    gav, nav_per_share = get_value(
        vault_proxy,
        addresses["USDT"],
    )
    FundPrice.objects.create(
        fund=Fund.objects.get(vault_proxy=vault_proxy),
        gav=gav,
        nav_per_share=nav_per_share,
    )


def update_funds_price():
    funds = list(Fund.objects.all())
    for fund in funds:
        add_price_to_fund(fund.vault_proxy)
