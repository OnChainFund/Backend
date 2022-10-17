# pyright: strict
"""
步驟：
    1. 獲得各資產權重(如果是負數,則換成reverse token)
    2. 獲得 dex 上各資產價格
    3. 獲得目前 fund 中的各資產權重
    4. 計算調倉路徑
    """

from fund.tasks import get_fund_gav
from utils.ai.get_balance_multicall import get_balance_multicall
from utils.ai.get_weighted_positions import get_weighted_positions
from utils.data_source.ftx.get_price_ftx import (
    get_price_ftx_for_all_asset_in_input_list,
)

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
print("================================================================")
print(get_weighted_positions())
print("================================================================")
print(get_balance_multicall(fund_address))
# 2. 獲得 ftx 上各資產價格
dex_price_list_positive = get_price_ftx_for_all_asset_in_input_list(targets)
dex_price_list_all: list[float] = []
for i in dex_price_list_positive:
   dex_price_list_all.extend([i,]) 



# 3. 獲得目前 fund 中的總價值
print("================================================================")
print(get_fund_gav(fund_address))
# 4. 獲得
