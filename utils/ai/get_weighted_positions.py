# pyright: strict
from eth_typing.evm import Address
from eth_utils.address import to_canonical_address
import pandas as pd
from management.weight.model import *
from datetime import datetime
from pydantic import BaseModel
from utils.ai.get_weights import get_weights






class Position(BaseModel):
    token_name: str
    token_address: Address
    weight: int


def get_weighted_positions() -> list[Position]:
    now = pd.Timestamp.now().round("60min").to_pydatetime()
    now = int(datetime.timestamp(now))
    weight = get_weights()
    weights = weight
    positions: list[Position] = []
    for i in range(0, len(assets)):
        # print(weights[i])
        if weights[i] > 0:
            positions.append(
                Position(
                    token_name=assets[i]["positive"]["name"],
                    token_address=to_canonical_address(
                        assets[i]["positive"]["address"]
                    ),
                    weight=weights[i] * 10000,
                )
            )
        else:
            positions.append(
                Position(
                    token_name=assets[i]["negitive"]["name"],
                    token_address=to_canonical_address(
                        assets[i]["negitive"]["address"]
                    ),
                    weight=weights[i] * 10000,
                )
            )
    return positions
