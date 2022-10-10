from math import ceil, floor
import pandas as pd
from management.weight.model import *
from datetime import datetime

from management.weight.run_weights import get_weights

now = pd.Timestamp.now().round("60min").to_pydatetime()
now = int(datetime.timestamp(now))
weight = get_weights(now, 3600)
weights = weight.iloc[-1, :].to_numpy()  # type: ignore
for i in weights:
    print(int(i * 100000))
