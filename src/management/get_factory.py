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


def get_factory():

    # denominated_asset = Addresses["AVAXDOWN"]
    pair_list = [
        "0x10e87C2dADe91407b3f5284196fd29E3810EDd28",
        "0x4AC3d002400311F189055a37FD167957F62C7833",
        "0xA322A4ee52bC8D59fc08d4E53Be62b4eB15a3cc8",
        "0xaE397bA5C8d6db0551682747CD2d10c7C312792D",
        "0x067fFF03C2927C386fadb1E17eCb5e8D45d47140",
        "0xF4C8dcF69B4659aB1A2383Db99fb5b2f5cf033FB",
        "0xA0ec06573965bd4b4d98d294650Cc36991217B0C",
        "0xfD285A591369d15575f2471577ba6Bc0553ec261",
        "0x6cCb936649876Cd8a33245Dd7A0a53Be12702F1d",
        "0xf49f6045324CeeB5d5024FE4a22aF58e096e8C01",
        "0x3d99134b50Be0E6BD552d04BAED93D6f91aF9e07",
        "0xbEC5d86a46f03D8687CC477D21Cf839459d8C32f",
        "0x795A3E99008d09e3DE68CCb348A8ACcdc0177996",
        "0x2c2BC524b58D79aa029eBaa8ce3F1e34274E1712",
        "0x7ba3e44FcD1952CCE2dc3EA0DE1D8b85A13f58b2",
        "0x62e43940a15599F3930F6658Ac627a3aa187A873",
        "0xBf28854efA97faA827148dEB39383CbCb28e461e",
        "0x9549746CAd0BB08D0E3cABC272392FE060966721",
        "0xf3d1655590a5A6ACAAb773FbB5d8445799772392",
        "0xaA50201722D6B0D0638999d9901264055750a71E",
        "0xd2b6B3264b90337aCc03e616309A2a85C0C0A410",
        "0x6fBdf08062B79c90e9023C3f91cC4E66200c7986",
    ]
    w3 = get_provider()

    for pair in pair_list:
        pangolin_pair = w3.eth.contract(
            # Addresses["pangolinFactory"], abi=PangolinFactory
            pair,
            abi=PangolinPair,
        )
        pangolin_pair_contract = w3.eth.contract(
            pair,
            abi=PangolinPair,
        )
        # 獲取流動性對的剩餘量
        print(pangolin_pair_contract.functions.factory().call())


get_factory()
