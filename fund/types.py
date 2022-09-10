# types.py
import strawberry
from strawberry import auto
from typing import List
from . import models


@strawberry.django.type(models.Price)
class Price:
    id: auto
    date: auto
    price: auto
    fund: "Fund"


@strawberry.django.type(models.Fund)
class Fund:
    vault_proxy: auto
    comptroller_proxy: auto
    name: auto
    denominated_asset: "Asset"
    creator: auto
    depositors: auto
    price: List[Price]


@strawberry.django.type(models.Asset)
class Asset:
    address: auto
    name: auto
    funds: List[Fund]
