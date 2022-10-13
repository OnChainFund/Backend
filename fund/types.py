import datetime
import json
import time
from eth_abi.abi import decode
from eth_utils.address import to_canonical_address
from pydantic import BaseModel
import requests
import strawberry
from strawberry import auto
from typing import Any, List
import strawberry.django
from abi.ocf.ComptrollerLib import ComptrollerLib
from abi.ocf.VaultLib import VaultLib
from utils.multicall.multicall import Multicall
import pandas as pd
from utils.utils import get_provider
from . import models

# filters
@strawberry.django.filters.filter(models.FundPrice, lookups=True)
class FundPriceFilter:
    id: auto
    time: auto
    gav: auto
    nav_per_share: auto
    fund: "Fund"


@strawberry.django.filters.filter(models.Fund, lookups=True)
class FundFilter:
    vault_proxy: auto
    comptroller_proxy: auto
    name: auto
    denominated_asset: auto
    creator: auto
    depositors: auto
    detail: auto
    price: FundPriceFilter


@strawberry.django.filters.filter(models.Fund, lookups=True)
class FundFilterForCreator:
    creator: auto
    vault_proxy: auto


@strawberry.django.filters.filter(models.Asset, lookups=True)
class AssetFilterForAddress:
    address: auto
    name: auto


#
#    def filter_creator(self, queryset):
#
#        return queryset.filter(creator=self.creator)


@strawberry.django.filters.filter(models.Fund, lookups=True)
class FundUpdateFilter:
    vault_proxy: auto


@strawberry.django.filters.filter(models.AssetPrice, lookups=True)
class AssetPriceFilter:
    id: auto
    time: auto
    price: auto
    asset: "Asset"


@strawberry.django.filters.filter(models.Asset, lookups=True)
class AssetFilter:
    address: auto
    name: auto
    price: AssetPriceFilter
    funds: FundFilter


# order
@strawberry.django.ordering.order(models.FundPrice)
class FundPriceOrder:
    id: auto
    fund: "Fund"


@strawberry.django.ordering.order(models.Fund)
class FundOrder:
    name: auto
    price: FundPriceOrder


@strawberry.django.ordering.order(models.AssetPrice)
class AssetPriceOrder:
    id: auto
    asset: "Asset"


@strawberry.django.ordering.order(models.Asset)
class AssetOrder:
    name: auto
    price: AssetPriceOrder
    funds: FundOrder


# types
@strawberry.django.type(models.FundPrice)
class FundPrice:
    id: auto
    time: auto
    gav: auto
    nav_per_share: auto
    fund: "Fund"


class FundInfoModel(BaseModel):
    symbol: str
    name: str
    denominated_asset: str


@strawberry.experimental.pydantic.type(model=FundInfoModel, all_fields=True)
class FundInfo:
    pass


@strawberry.django.type(models.Fund)
class Fund:
    vault_proxy: auto
    comptroller_proxy: auto
    name: auto
    description: auto
    detail: auto
    denominated_asset: auto
    creator: auto
    depositors: auto
    price: List["FundPrice"]

    @strawberry.django.field
    def depositor_count(self) -> int:
        return self.depositors.through.objects.count()

    @strawberry.django.field
    def fund_info(self) -> FundInfo:
        w3 = get_provider()
        multicall = Multicall(w3, "fuji")
        vault = w3.eth.contract(
            to_canonical_address(self.vault_proxy),
            abi=VaultLib,
        )
        comptroller = w3.eth.contract(
            to_canonical_address(self.comptroller_proxy),
            abi=ComptrollerLib,
        )
        calls = [
            multicall.create_call(
                vault,
                "symbol",
                [],
            ),
            multicall.create_call(
                vault,
                "name",
                [],
            ),
            multicall.create_call(
                comptroller,
                "getDenominationAsset",
                [],
            ),
        ]

        result = multicall.call(calls)

        return FundInfoModel(
            symbol=decode(["string"], result[1][0])[0],
            name=str(decode(["string"], result[1][1])[0]),
            denominated_asset=str(decode(["address"], result[1][2])[0]),
        )


@strawberry.django.type(models.AssetPrice)
class AssetPrice:
    id: auto
    time: auto
    price: auto
    asset: "Asset"

    @strawberry.django.field
    def value(self) -> float:
        return self.price


class BasePriceInfoModel(BaseModel):
    # time: datetime.datetime
    time: str
    value: float


@strawberry.experimental.pydantic.type(model=BasePriceInfoModel, all_fields=True)
class BasePriceInfo:
    pass


@strawberry.django.type(models.Asset)
class Asset:
    address: auto
    name: auto
    price: List["AssetPrice"]
    funds: List["Fund"]

    @strawberry.django.field
    def ftx_price(self) -> list[BasePriceInfo]:
        url = "https://ftx.com/api"
        resolution = 3600 * 24
        end_time = int(time.time())
        start_time = end_time - (100 * resolution)
        api = f"/markets/AAPL/USD/candles?resolution={resolution}&start_time={start_time}&end_time={end_time}"
        res = requests.get(url + api).json()
        df = pd.DataFrame(res["result"])
        # df.drop(columns=["time","volume"])
        k = df.drop(["time", "volume", "open", "high", "low"], axis=1)
        start_time = k["startTime"].values.tolist()
        close = k["close"].values.tolist()
        results: list[BasePriceInfo] = []

        for i in range(len(start_time)):
            results.append(BasePriceInfo(time=start_time[i], value=close[i]))

        return results


# input types
@strawberry.django.input(models.Fund)
class FundInput:
    vault_proxy: auto
    comptroller_proxy: auto
    name: auto
    description: auto
    denominated_asset: auto
    creator: auto
    depositors: auto


@strawberry.django.input(models.Fund)
class FundInputForFilter:
    creator: auto


@strawberry.django.input(models.Asset)
class AssetInput:
    # address: auto
    name: auto


# partial input types
@strawberry.django.input(models.Fund, partial=True)
class FundPartialInput(FundInput):
    name: auto
    description: auto
    detail: auto


@strawberry.django.input(models.Asset, partial=True)
class AssetPartialInput(AssetInput):
    pass
