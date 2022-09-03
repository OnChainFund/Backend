from ast import Add
from datetime import timezone
from decouple import config

from utils.data_source.ftx.client import FtxClient
from utils.utils import get_provider
from contract.contracts.deployment.others.PangolinFactory import PangolinFactory
from contract.contracts.deployment.others.PangolinRouter import PangolinRouter
from contract.contracts.deployment.others.Addresses import Addresses


def manage_liquidity():
    print("managed liquidity")
    # 用 ftx api 獲取價格資料

    ftx_client = FtxClient()
    data = ftx_client.get_price("ETH/USD")
    # 從 pangolin swap 獲取流動性資料
    # 獲取 pair address(pangolinFactory.getPair)
    w3 = get_provider()
    pangolin_factory = w3.eth.contract(
        Addresses["pangolinFactory"], abi=PangolinFactory
    )
    pangolin_router = w3.eth.contract(Addresses["pangolinRouter"], abi=PangolinRouter)
    # get Researve 獲取比例
    print(
        pangolin_factory.functions.getPair(Addresses["USDT"], Addresses["WETH"]).call()
    )

    # 計算出價格
    # 計算 swap input,output
    # swap

    private_key = config("PRIVATE_KEY")

    txn = pangolin_router.functions.swapExactTokensForTokens(
        10000,
        1,
        [Addresses["USDT"], Addresses["WAVAX"]],
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
    print(signed_txn.rawTransaction)
    print(dir(signed_txn))
    w3.eth.sendRawTransaction(signed_txn.rawTransaction)


manage_liquidity()
