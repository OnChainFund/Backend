from math import floor
import os
from pprint import pprint
from django.conf import settings
import pandas as pd
from psycopg2 import Timestamp
import requests
from collections import OrderedDict
import numpy as np
import torch
from torch.utils.data import Dataset, DataLoader
from tqdm import tqdm
from management.weight.model import *
from datetime import datetime

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
resolution = 3600  # per hour
name = "BTC/USD"
now = pd.Timestamp.now().round("60min").to_pydatetime()
now = int(datetime.timestamp(now))
start_time = now - 5 * resolution
end_time = now
api = f"/markets/{name}/candles?resolution={resolution}&start_time={start_time}&end_time={end_time}"
res = requests.get(url + api).json()
pprint(res)
