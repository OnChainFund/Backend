from ast import Add
from datetime import timezone
import math
from decouple import config
from graphql import assert_list_type

from utils.data_source.ftx.client import FtxClient
from utils.utils import get_provider
from contract.contracts.deployment.others.PangolinFactory import PangolinFactory
from contract.contracts.deployment.others.PangolinRouter import PangolinRouter
from contract.contracts.deployment.others.PangolinPair import PangolinPair
from contract.contracts.deployment.others.Addresses import Addresses
from contract.contracts.deployment.others.ERC20 import ERC20


def get_price_from_ftx(ftx_trading_pair: str) -> int:
    ftx_client = FtxClient()
    data = ftx_client.get_price(ftx_trading_pair)
    return data


def get_lp():

    target_asset = Addresses["USDT"]
    # denominated_asset = Addresses["AVAXDOWN"]
    asset_list = [
        "0x6cEeB8fec16F7276F57ACF70C14ecA6008d3DDD4",
        "0xE85e1219691aF541F064E111161174C1F7Db2e84",
        #  "0xB7B8E01a9F5dFe405c37b667E8F81a66D4f629EA",
        #  "0x7f5BE805EFdbc5b42A3cfBC41B2961A0A9d9e3B2",
        #  "0x0690b3F6f8271b000f800F051f82B65F41D29C5E",
        #  "0xC7c69FFC3561fb3284F4d6D25d8b69D8CB3b59e9",
        #  "0xe05F46AAfa9919f722bc83fbD2Bb7B3Ac23E1Bc2",
        #  "0xFb1438372dB41dAFFcf4019e80eAE2D673B8c3b7",
        #  "0xa19baf63747637D0233702bA8F1eFcD6729db4DF",
        #  "0xA964EeaE6e77B1d01432942bc31186cB56eA5804",
        #  "0x33506d382684db988D9021A80dBEeEF46a5ABC3A",
    ]
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
    for asset in asset_list:
        pair = pangolin_factory.functions.getPair(target_asset, asset).call()
        # pangolin_pair_contract = w3.eth.contract(
        #     pair,
        #     abi=PangolinPair,
        # )
        # 獲取流動性對的剩餘量
        # print(pangolin_pair_contract.factory().call())
        print(pair)


get_lp()
