from datetime import timezone
from decouple import config

from utils.data_source.ftx.client import FtxClient
from utils.utils import get_provider
from contract.contracts.deployment.others.PangolinFactory import PangolinFactory
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
    # get Researve 獲取比例
    print(
        pangolin_factory.functions.getPair(Addresses["USDT"], Addresses["WETH"]).call()
    )

    # 計算出價格
    # 計算 swap input,output
    # swap
    private_key = config("PRIVATE_KEY")


manage_liquidity()
