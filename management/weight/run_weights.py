from math import floor
import os
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


## Start time
####
def get_weights(time: Timestamp, resolution: int) -> list:

    start_time = time - 479 * resolution
    print(f'{"start":<8}:', datetime.fromtimestamp(start_time))
    print(f'{"end":<8}:', datetime.fromtimestamp(time))

    ## collecting data
    l = []
    pbar = tqdm(total=len(target), colour="green", ncols=100, position=0, leave=True)
    for name in target:

        api = f"/markets/{name}/candles?resolution={resolution}&start_time={start_time}&end_time={time}"
        res = requests.get(url + api).json()
        df = pd.DataFrame(res["result"])
        l.append(df["close"])
        pbar.set_postfix(symbol=name)
        pbar.update(1)
    pbar.close()
    data = pd.concat(l, axis=1)
    data.index = df["startTime"]
    data.columns = target
    data.fillna(method="ffill", inplace=True)

    ###weight_generation
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    model = CNNTransformer(
        os.path.join(settings.MEDIA_ROOT, "checkpoints/"),
        lookback=360,
        num_of_assets=len(target),
        out=out_layer,
    )

    checkpoint = torch.load(check_path, map_location=device)
    newkeys = [k[7:] for k in list(checkpoint["model_state_dict"].keys())]
    check = OrderedDict(zip(newkeys, list(checkpoint["model_state_dict"].values())))
    bs = 32 if torch.cuda.is_available() else 1
    loader = prep_dataloader(data, lookback=360, holding=0, batch_size=bs)
    _, _, day_index = preprocess_log_return(data, lookback=360, holding=0)
    model.load_state_dict(check)
    model.to(device)
    model.eval()
    weight = []
    with torch.no_grad():
        for x, y in loader:
            x = x.flatten(0, 1)
            x, y = x.to(device), y.to(device)
            out = model(x)
            out = out.cpu().detach().numpy().tolist()
            weight = weight + out
    df_weight = pd.DataFrame(weight, index=day_index, columns=target)
    return df_weight


# filepath = './Data/'
def preprocess_log_return(data, lookback=240, holding=120):
    """
    Preprocess TxN numpy ndarray `data` into log return windows of integer length `lookback`(train_x).
    and log return windows of integer length `holding`(train_y)
    """
    # df = pd.read_csv(data, index_col = 0, parse_dates = True)
    df = data
    T, N = df.shape
    time_line = df.index
    log_data = np.log(df) - np.log(df.shift(1))
    date = log_data.index[lookback : T - holding]
    log_data_ = log_data.iloc[1:, :].to_numpy()
    windows_x = []
    windows_y = []
    for t in range(lookback, T - holding):
        windows_x.append(log_data_[t - lookback : t, :].T)
        windows_y.append(log_data_[t : t + holding, :].T)

    windows_x = np.array(windows_x, dtype=np.float32)
    windows_y = np.array(windows_y, dtype=np.float32)
    print("x shape:", windows_x[0].shape)
    print("y shape:", windows_y[0].shape)
    # np.save(filepath + 'train_x_.npy', windows_x)
    # np.save(filepath + 'train_y_.npy', windows_y)
    return windows_x, windows_y, date


class Crypto(Dataset):
    def __init__(self, path, lookback=720, holding=120):
        # logging.info("Data loading...")
        dx, dy, self.date = preprocess_log_return(path, lookback, holding)
        # logging.info(f"Data loaded.")
        # logging.info(f"Training data X shape: {dx.shape}")
        # logging.info(f"Training data Y shape: {dy.shape}")
        self.tx = torch.FloatTensor(dx)
        self.ty = torch.FloatTensor(dy)
        self.n = dx.shape[0]

    def __getitem__(self, index):
        return self.tx[index], self.ty[index]

    def __len__(self):
        return self.n


def prep_dataloader(path, lookback=720, holding=120, batch_size=32):
    """Generates a dataset, then is put into a dataloader."""
    dataset = Crypto(path, lookback, holding)  # Construct dataset
    dataloader = DataLoader(
        dataset, batch_size, shuffle=False, drop_last=False, pin_memory=True
    )  # Construct dataloader
    return dataloader
