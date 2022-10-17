from fund.models import Asset, AssetPrice
from utils.data_source.ftx.client import FtxClient


def get_price_from_ftx(ftx_trading_pair: str, is_short_position: bool = False) -> float:
    ftx_client = FtxClient()
    data = ftx_client.get_price(ftx_trading_pair)
    try:
        value = float(data)
    except ValueError:
        value = 0
    if is_short_position:
        data = 10000 / value
    return value


def get_price_from_ftx_both(ftx_trading_pair: str) -> tuple[float, float]:
    ftx_client = FtxClient()
    data = ftx_client.get_price(ftx_trading_pair)
    try:
        value = float(data)
    except ValueError:
        value = 0
    short_position_data = 10000 / value
    return (value, short_position_data)


def add_asset_price_to_db(target_asset_address: str, ftx_price: float):
    asset = Asset.objects.get(pk=target_asset_address)
    asset_price = AssetPrice(asset=asset, price=ftx_price)
    asset_price.save()
