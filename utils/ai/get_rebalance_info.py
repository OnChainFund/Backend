# pyright: strict
"""
步驟：
    1. 獲得各資產權重(如果是負數,則換成reverse token)
    2. 獲得 dex 上各資產價格
    3. 獲得目前 fund 中的各資產權重
    4. 計算調倉路徑
    """

from datetime import datetime
from pprint import pprint
import pandas as pd
from pydantic.main import BaseModel
from fund.models import Asset

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
def get_rebalance_goal_info(fund_address: str, buffer: float):
    """獲取重新調倉的目標部位

    Args:
        fund_address (str): 基金地址
        buffer (float): 緩衝區比例
    """
    now = pd.Timestamp.now().round("60min").to_pydatetime()
    now = int(datetime.timestamp(now))
    weight = get_weights()
    # print(weight)
    weights = weight
    weight_include_negative_position: list[float] = []
    for i in weights:
        if i < 0:
            weight_include_negative_position.extend([0, -i])
        else:
            weight_include_negative_position.extend([i, 0])

    # 2. 獲得 ftx 上各資產價格
    dex_price_list_all: list[float] = []
    for target in targets:
        (positive_portion_price, negative_portion_price) = get_price_from_ftx_both(
            target
        )
        dex_price_list_all.extend([positive_portion_price, negative_portion_price])
    # print(dex_price_list_all)
    # 3. 獲得目前 fund 中的總價值
    print("================================================================")
    fund_gav = get_fund_gav(fund_address)
    # 獲得資產數目(應得)-> weight*(aum of fund)*(asset price)
    target_fund_assets_amounts: list[float] = []
    print((dex_price_list_all))
    print((weight_include_negative_position))
    # print((fund_assets_balance))

    for i in range(0, len(dex_price_list_all)):
        target_fund_assets_amounts.append(
            weight_include_negative_position[i]
            * fund_gav
            * (1 - buffer)
            / dex_price_list_all[i]
        )
    return target_fund_assets_amounts


target_fund_assets_amounts = get_rebalance_goal_info(fund_address, 0.1)

for i in range(0, len(target_fund_assets_amounts)):
    print(targets[i // 2], end=" ")
    print(target_fund_assets_amounts[i])

fund_assets_balance = get_balance_multicall(fund_address)
print(fund_assets_balance)
