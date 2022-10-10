import os
from django.conf import settings
import pandas as pd
import requests
from management.weight.model import *
from datetime import datetime
from .models import Asset

url = "https://ftx.com/api"
out_layer = "origin"
check_path = os.path.join(settings.MEDIA_ROOT, "checkpoints/model_weight.tar")
target = [
    "BTC/USD",
    "ETH/USD",
    "USDT/USD",
    "AAVE/USD",
    "AAPL/USD",
    "TWTR/USD",
    "GLD/USD",
    "TSLA/USD",
    "LINK/USD",
    "AVAX/USD",
]


def get_price_ftx(from_asset_address: str, to_asset_address: str):
    from_asset = Asset.objects.all.filter(address=from_asset_address)
    resolution = 3600  # per hour
    name = "BTC/USD"
    now = pd.Timestamp.now().round("60min").to_pydatetime()
    now = int(datetime.timestamp(now))
    start_time = now - 5 * resolution
    end_time = now
    api = f"/markets/{name}/candles?resolution={resolution}&start_time={start_time}&end_time={end_time}"
    res = requests.get(url + api).json()
    df = pd.DataFrame(res["result"])
    df.drop(columns=["open", "low"])
    print(df)


get_price_ftx(
    "0xe05F46AAfa9919f722bc83fbD2Bb7B3Ac23E1Bc2",
    "0xE85e1219691aF541F064E111161174C1F7Db2e84",
)
