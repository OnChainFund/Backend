from fund.models import Asset, AssetPrice
from utils.data_source.ftx.client import FtxClient


def get_price_from_ftx(ftx_trading_pair: str, is_short_position: bool = False) -> int:
    ftx_client = FtxClient()
    data = ftx_client.get_price(ftx_trading_pair)
    if is_short_position:
        data = 10000 / data
    return data


def get_price_from_ftx_both(ftx_trading_pair: str) -> int:
    ftx_client = FtxClient()
    data = ftx_client.get_price(ftx_trading_pair)
    short_position_data = 10000 / data
    return data, short_position_data


def add_asset_price_to_db(target_asset_address: str, ftx_price: float):
    asset = Asset.objects.get(pk=target_asset_address)
    asset_price = AssetPrice(asset=asset, price=ftx_price)
    asset_price.save()
