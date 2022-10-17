# pyright: strict
"""
步驟：
    1. 獲得各資產權重(如果是負數,則換成reverse token)
    2. 獲得 dex 上各資產價格
    3. 獲得目前 fund 中的各資產權重
    4. 計算調倉路徑
    """

from datetime import datetime
from numpy import negative
import pandas as pd
from fund.tasks import get_fund_gav
from utils.ai.get_balance_multicall import get_balance_multicall
from utils.ai.get_weighted_positions import get_weighted_positions
from utils.ai.get_weights import get_weights
from utils.data_source.ftx.utils import get_price_from_ftx_both

targets = [
    "AAPL/USD",
    "AAVE/USD",
    "AVAX/USD",
    "BTC/USD",
    "ETH/USD",
    "GLD/USD",
    "LINK/USD",
    "TSLA/USD",
    "TWTR/USD",
    "USDT/USD",
]
fund_address = "0xdB15F01C3C7Dd083e0434Dd09E740ca3906Ab41c"
# 1. 獲得各資產權重(如果是負數,則換成reverse token)
asset_weight = get_weighted_positions()

fund_assets_balance = get_balance_multicall(fund_address)
# 2. 獲得 ftx 上各資產價格
dex_price_list_all: list[float] = []
for target in targets:
    (positive_portion_price, negative_portion_price) = get_price_from_ftx_both(target)
    dex_price_list_all.extend([positive_portion_price, negative_portion_price])
print(dex_price_list_all)
# 3. 獲得目前 fund 中的總價值
print("================================================================")
print(get_fund_gav(fund_address))
# 獲得資產數目(應得)-> weight*(aum of fund)*(asset price)
target_fund_assets_amounts = []
print(len(dex_price_list_all))
print(len(asset_weight))
print(len(fund_assets_balance))
for i in range(0, len([])):
    pass
