from fund.models import Asset, AssetPrice
from utils.data_source.ftx.client import FtxClient


def add_asset_price_to_db(target_asset_address: str, ftx_price: float):
    asset = Asset.objects.get(pk=target_asset_address)
    asset_price = AssetPrice(asset=asset, price=ftx_price)
    asset_price.save()
