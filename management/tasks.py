from ast import Add
from datetime import timezone
import math
from decouple import config

from utils.data_source.ftx.client import FtxClient
from utils.utils import get_provider
from contract.contracts.deployment.others.PangolinFactory import PangolinFactory
from contract.contracts.deployment.others.PangolinRouter import PangolinRouter
from contract.contracts.deployment.others.PangolinPair import PangolinPair
from contract.contracts.deployment.others.Addresses import Addresses


def get_price_from_ftx(ftx_trading_pair: str) -> int:
    ftx_client = FtxClient()
    data = ftx_client.get_price(ftx_trading_pair)
    return data


def manage_liquidity(
    target_asset: str, denominated_asset: str, ftx_trading_pair: str, price: int
):
    print("managed liquidity")
    # 用 ftx api 獲取價格資料
    ftx_price = get_price_from_ftx(ftx_trading_pair)
    print(ftx_price)
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

    pair = pangolin_factory.functions.getPair(target_asset, denominated_asset).call()
    print(pair)
    pangolin_pair = w3.eth.contract(pair, abi=PangolinPair)
    # 獲取流動性對的剩餘量
    (
        reserve0,
        reserve1,
        blockTimestampLast,
    ) = pangolin_pair.functions.getReserves().call()
    print(reserve0)
    print(reserve1)
    token0 = pangolin_pair.functions.token0().call()
    token1 = pangolin_pair.functions.token1().call()
    # 計算出價格
    if target_asset == token0:
        print("target = 0")
        pangolin_price = reserve1 / reserve0
        reserve_target_asset = reserve0
        reserve_denominated_asset = reserve1
        # pangolin_price = pangolin_pair.functions.price0CumulativeLast().call()

    elif target_asset == token1:
        print("target = 1")
        pangolin_price = reserve0 / reserve1
        reserve_target_asset = reserve1
        reserve_denominated_asset = reserve0
        # pangolin_price = pangolin_pair.functions.price1CumulativeLast().call()
    print(pangolin_price)

    if pangolin_price <= ftx_price:
        print("buy target")
        amount = reserve_target_asset - math.sqrt(
            reserve_target_asset * reserve_denominated_asset * ftx_price
        )
        path = [denominated_asset, target_asset]
    else:
        print("sell target")
        amount = (
            math.sqrt(reserve_target_asset * reserve_denominated_asset * ftx_price)
            - reserve_target_asset
        )
        path = [target_asset, denominated_asset]
    # 計算 swap input,output
    # swap
    print(int(amount))
    private_key = config("PRIVATE_KEY")

    txn = pangolin_router.functions.swapExactTokensForTokens(
        int(amount),
        1,
        path,
        Addresses["user_1"],
        1758392484,
    ).buildTransaction(
        {
            "chainId": 43113,
            "gas": 7900000,
            "maxFeePerGas": w3.toWei("30", "gwei"),
            "maxPriorityFeePerGas": w3.toWei("1", "gwei"),
            "nonce": w3.eth.getTransactionCount(Addresses["user_1"]),
        }
    )
    signed_txn = w3.eth.account.sign_transaction(txn, private_key=private_key)
    # w3.eth.sendRawTransaction(signed_txn.rawTransaction)


manage_liquidity(Addresses["WAVAX"], Addresses["USDT"], "AVAX/USD", 1)
