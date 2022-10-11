# pyright: strict
"""
步驟：
    1. 獲得各資產權重(如果是負數,則換成reverse token)
    2. 獲得 dex 上各資產價格
    3. 獲得目前 fund 中的各資產權重
    4. 計算調倉路徑
    """

from utils.ai.get_balance_multicall import get_balance_multicall
from utils.ai.get_pangolin_price_multicall import get_pangolin_price_multicall
from utils.ai.get_weighted_positions import get_weighted_positions

# 1. 獲得各資產權重(如果是負數,則換成reverse token)
print(get_weighted_positions())
# 2. 獲得 dex 上各資產價格
# 3. 獲得目前 fund 中的各資產權重
print(get_balance_multicall("0x9dd3b3471AF147DF6c7E93ff35a5f04eE9342e9C"))

print(get_pangolin_price_multicall("0x9dd3b3471AF147DF6c7E93ff35a5f04eE9342e9C"))
