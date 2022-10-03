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

from management.weight.run_weights import get_weights


now = pd.Timestamp.now().round("60min").to_pydatetime()
now = int(datetime.timestamp(now))
weight = get_weights(now, 3600)
weights = weight.iloc[-1, :].to_numpy()
for i in weights:
    print(floor(i * 100000))