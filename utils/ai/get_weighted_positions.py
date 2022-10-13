# pyright: strict
from eth_typing.evm import Address
from eth_utils.address import to_canonical_address
import pandas as pd
from management.weight.model import *
from datetime import datetime
from pydantic import BaseModel
from utils.ai.get_weights import get_weights


token = dict[str, str]
assets: list[dict[str, str | token]] = [
    {
        "ftx_pair_name": "AAPL/USD",
        "negitive": {
            "address": "0xC7c69FFC3561fb3284F4d6D25d8b69D8CB3b59e9",
            "name": "AAPLDOWN",
        },
        "positive": {
            "address": "0x930b24b4b578409153501429cc256FBbDAB6e893",
            "name": "AAPL",
        },
    },
    {
        "ftx_pair_name": "AAVE/USD",
        "negitive": {
            "address": "0x0690b3F6f8271b000f800F051f82B65F41D29C5E",
            "name": "AAVEDOWN",
        },
        "positive": {
            "address": "0x9Bb8F40d53DA2796F34d85f5bf27C475Df03E70C",
            "name": "AAVE",
        },
    },
    {
        "ftx_pair_name": "AVAX/USD",
        "negitive": {
            "address": "0x33506d382684db988D9021A80dBEeEF46a5ABC3A",
            "name": "AVAXDOWN",
        },
        "positive": {
            "address": "0x6cEeB8fec16F7276F57ACF70C14ecA6008d3DDD4",
            "name": "AVAX",
        },
    },
    {
        "ftx_pair_name": "BTC/USD",
        "negitive": {
            "address": "0xE85e1219691aF541F064E111161174C1F7Db2e84",
            "name": "BTCDOWN",
        },
        "positive": {
            "address": "0xbC9052c594261Acc1a26271567bDb72A8A1Acac9",
            "name": "BTC",
        },
    },
    {
        "ftx_pair_name": "ETH/USD",
        "negitive": {
            "address": "0xB7B8E01a9F5dFe405c37b667E8F81a66D4f629EA",
            "name": "ETHDOWN",
        },
        "positive": {
            "address": "0x96058B65CE7d0DBa4B85DAf49E06663B97442137",
            "name": "ETH",
        },
    },
    {
        "ftx_pair_name": "GLD/USD",
        "negitive": {
            "address": "0xFb1438372dB41dAFFcf4019e80eAE2D673B8c3b7",
            "name": "GLDDOWN",
        },
        "positive": {
            "address": "0x7D157E24f3D6FB7Bd8B3008A76DFBCde267daCa8",
            "name": "GLD",
        },
    },
    {
        "ftx_pair_name": "LINK/USD",
        "negitive": {
            "address": "0xA964EeaE6e77B1d01432942bc31186cB56eA5804",
            "name": "LINKDOWN",
        },
        "positive": {
            "address": "0x5B3a2CAED90515e36830167529AFeDea75419b7a",
            "name": "LINK ",
        },
    },
    {
        "ftx_pair_name": "TSLA/USD",
        "negitive": {
            "address": "0xa19baf63747637D0233702bA8F1eFcD6729db4DF",
            "name": "TSLADOWN",
        },
        "positive": {
            "address": "0x22044e0e4E2D774f34227FC8a1BF804Ff9Fc9A35",
            "name": "TSLA",
        },
    },
    {
        "ftx_pair_name": "TWTR/USD",
        "negitive": {
            "address": "0xe05F46AAfa9919f722bc83fbD2Bb7B3Ac23E1Bc2",
            "name": "TWTRDOWN",
        },
        "positive": {
            "address": "0x181Bf62B82AFafa87630C819482ABbA819e49601",
            "name": "TWTR",
        },
    },
    {
        "ftx_pair_name": "USDT/USD",
        "negitive": {
            "address": "0x7f5BE805EFdbc5b42A3cfBC41B2961A0A9d9e3B2",
            "name": "USDTDOWN",
        },
        "positive": {
            "address": "0xd1Cc87496aF84105699E82D46B6c5Ab6775Afae4",
            "name": "USDT",
        },
    },
]


class Position(BaseModel):
    token_name: str
    token_address: Address
    weight: int


def get_weighted_positions() -> list[Position]:
    now = pd.Timestamp.now().round("60min").to_pydatetime()
    now = int(datetime.timestamp(now))
    weight = get_weights(now, 3600)
    weights = weight.iloc[-1, :].to_numpy()  # type: ignore
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
