from utils.ai.constants import assets
from utils.ai.get_weights import get_weights_with_asset_address
from math import sqrt
from abi.others.ERC20 import ERC20 as ERC20_ABI
from abi.others.PangolinRouter import PangolinRouter
from management.models import PriceManagement
from utils.constants.addresses import addresses
from utils.data_source.ftx.utils import get_price_from_ftx
from utils.multicall.multicall import Multicall
from utils.multicall.multicall_write import MulticallWrite
from utils.utils import get_provider

w3 = get_provider()

multicall = Multicall(w3, "fuji")
multicall_write = MulticallWrite(w3, "fuji")
GAV = 100100
Buffer = 0.1
for key, value in get_weights_with_asset_address().items():
    print(key, "->", value)
