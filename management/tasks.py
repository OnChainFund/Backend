import math
from decouple import config
from fund.models import Asset, AssetPrice
from management.web3.utils import update_oracle_answer

from utils.data_source.ftx.client import FtxClient
from utils.utils import get_provider
from contract.contracts.deployment.others.PangolinFactory import PangolinFactory
from contract.contracts.deployment.others.PangolinRouter import PangolinRouter
from contract.contracts.deployment.others.Addresses import Addresses
from contract.contracts.deployment.others.ERC20 import ERC20
from time import sleep


def get_price_from_ftx(ftx_trading_pair: str, is_short_position: bool) -> int:
    ftx_client = FtxClient()
    data = ftx_client.get_price(ftx_trading_pair)
    if is_short_position:
        data = 10000 / data
    return data


def manage_price(
    target_asset_address: str,
    denominated_asset_address: str,
    ftx_pair_name: str,
    mock_v3_aggregator_address: str,
    update_asset_price_db: bool,
    update_asset_price_pangolin: bool,
    update_asset_price_mock_v3_aggregator: bool,
    is_short_position: bool,
):
    # 用 ftx api 獲取價格資料

    ftx_price = get_price_from_ftx(ftx_pair_name, is_short_position)

    if update_asset_price_pangolin:
        manage_pangolin_liquidity(
            target_asset_address, denominated_asset_address, ftx_price
        )
    sleep(120)
    if update_asset_price_mock_v3_aggregator:
        update_oracle_answer(ftx_price, mock_v3_aggregator_address)
    sleep(120)
    # if update_asset_price_db:
    #    add_asset_price_to_db(target_asset_address, ftx_price)


def add_asset_price_to_db(target_asset_address: str, ftx_price: float):
    asset = Asset.objects.get(pk=target_asset_address)
    asset_price = AssetPrice(asset=asset, price=ftx_price)
    asset_price.save()
    pass


def manage_pangolin_liquidity(
    target_asset: str, denominated_asset: str, ftx_price: float
):

    # 從 pangolin swap 獲取流動性資料
    # 獲取 pair address(pangolinFactory.getPair)
    w3 = get_provider()
    pangolin_factory = w3.eth.contract(
        # Addresses["pangolinFactory"], abi=PangolinFactory
        Addresses["pangolin"]["FactoryMy"],
        abi=PangolinFactory,
    )
    pangolin_router = w3.eth.contract(
        Addresses["pangolin"]["Router"], abi=PangolinRouter
    )
    target_asset_contract = w3.eth.contract(target_asset, abi=ERC20)
    denominated_asset_contract = w3.eth.contract(denominated_asset, abi=ERC20)
    
    pair = pangolin_factory.functions.getPair(target_asset, denominated_asset).call()
    # 獲取流動性對的剩餘量

    target_asset_reserve = target_asset_contract.functions.balanceOf(pair).call()
    denominated_asset_reserve = denominated_asset_contract.functions.balanceOf(
        pair
    ).call()

    # 計算出價格
    pangolin_price = denominated_asset_reserve / target_asset_reserve
    # 差距小於 1% 不調倉
    if pangolin_price < ftx_price:
        amount = (
            math.sqrt(target_asset_reserve * denominated_asset_reserve * ftx_price)
            - denominated_asset_reserve
        )
        path = [denominated_asset, target_asset]
    else:
        print("sell target")
        print(math.sqrt(target_asset_reserve * denominated_asset_reserve * ftx_price))
        print(target_asset_reserve)
        amount = denominated_asset_reserve - math.sqrt(
            target_asset_reserve * denominated_asset_reserve * ftx_price
        )
        path = [target_asset, denominated_asset]

    # 計算 swap input,output
    # swap

    txn = pangolin_router.functions.swapExactTokensForTokens(
        int(abs(amount)),
        1,
        path,
        Addresses["user_1"],
        1758392484,
    ).buildTransaction(
        {
            "chainId": 43113,
            "gas": 7900000,
            # "maxFeePerGas": w3.toWei("30", "gwei"),
            # "maxPriorityFeePerGas": w3.toWei("1", "gwei"),
            "nonce": w3.eth.getTransactionCount(Addresses["user_1"]),
        }
    )
    signed_txn = w3.eth.account.sign_transaction(txn, private_key=config("PRIVATE_KEY"))
    w3.eth.sendRawTransaction(signed_txn.rawTransaction)


def calculate_weight():
    pass


def swap_fund_asset():
    pass


def rebalance():
    pass


# manage_pangolin_liquidity("0x6cEeB8fec16F7276F57ACF70C14ecA6008d3DDD4", "0xd1Cc87496aF84105699E82D46B6c5Ab6775Afae4", 18)
