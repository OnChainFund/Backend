# pyright: strict
"""
步驟：
    1. 獲得各資產權重(如果是負數,則換成reverse token)
    2. 獲得 dex 上各資產價格
    3. 獲得目前 fund 中的各資產權重
    4. 計算調倉路徑
    """

from utils.ai.get_balance_multicall import get_balance_multicall
from utils.ai.get_weighted_positions import get_weighted_positions

fund_address = "0x9dd3b3471AF147DF6c7E93ff35a5f04eE9342e9C"
# 1. 獲得各資產權重(如果是負數,則換成reverse token)
print(get_weighted_positions())
print(get_balance_multicall(fund_address))
# 2. 獲得 ftx 上各資產價格
# 3. 獲得目前 fund 中的總價值
# 4. 獲得
