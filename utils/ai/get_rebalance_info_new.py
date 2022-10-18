from datetime import datetime
from pprint import pprint

import pandas as pd
from djantic import ModelSchema
from pydantic.main import BaseModel

from fund.models import Asset, Fund
from fund.tasks import get_fund_gav
from management.models import Strategy
from utils.ai.get_balance_multicall import get_balance_multicall
from utils.ai.get_weighted_positions import get_weighted_positions
from utils.ai.get_weights import get_weights, get_weights_with_ftx_pair_name
from utils.data_source.ftx.utils import get_price_from_ftx_both


class AssetSchema(ModelSchema):
    class Config:
        model = Asset
        include = ["name", "address","ftx_pair_name","is_short_position"]

class FundSchema(ModelSchema):
    class Config:
        model = Fund
        include = ["vault_proxy", "comptroller_proxy","denominated_asset","subscribed_strategy"]


class AssetRebalanceInfo(BaseModel):
    asset: AssetSchema
    fund: FundSchema | None = None
    weight: float = 0.0
    balance_before_rebalance: float = 0.0
    balance_after_rebalance: float = 0.0


# strategy = Strategy.objects.first()
# weights = get_weights_with_ftx_pair_name()
asset_rebalance_info_list = []

# for fund in strategy.funds.all():
#    print("rebalance", end=" ")
#    print(fund)
#    for asset in strategy.assets.all():
#        # 如果是做空,加上權重又是負數就加入
#        if weights[asset.ftx_pair_name] < 0 and asset.is_short_position:
#            asset_rebalance_info_list.append(AssetRebalanceInfo(asset=asset, fund=fund))
#
fund = Fund.objects.first()
asset_1 = Asset.objects.first()
fund = FundSchema.from_orm(fund)
# a1 = AssetRebalanceInfo(
#    asset=AssetSchema.from_orm(asset_1), fund=FundSchema.from_orm(fund)
# )
# asset_rebalance_info_list.append(a1)
# print(asset_rebalance_info_list)
