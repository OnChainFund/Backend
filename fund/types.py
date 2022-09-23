import strawberry
from strawberry import auto
from typing import List
from django.contrib.auth import get_user_model
import strawberry_django
from . import models

# filters
@strawberry_django.filters.filter(models.Price, lookups=True)
class PriceFilter:
    id: auto
    date: auto
    gav: auto
    nav_per_share: auto
    fund: "Fund"


@strawberry_django.filters.filter(models.Fund, lookups=True)
class FundFilter:
    vault_proxy: auto
    comptroller_proxy: auto
    name: auto
    denominated_asset: "Asset"
    creator: auto
    depositors: auto
    price: PriceFilter


@strawberry_django.filters.filter(models.Asset, lookups=True)
class AssetFilter:
    address: auto
    name: auto
    funds: FundFilter


@strawberry_django.filters.filter(get_user_model(), lookups=True)
class UserFilter:
    # username: auto
    ethereum_address: auto
    # email: auto
    funds: FundFilter


# order
@strawberry_django.ordering.order(models.Price)
class PriceOrder:
    id: auto
    fund: "Fund"


@strawberry_django.ordering.order(models.Fund)
class FundOrder:
    name: auto
    price: PriceOrder


@strawberry_django.ordering.order(models.Asset)
class AssetOrder:
    name: auto
    funds: FundOrder


@strawberry_django.ordering.order(get_user_model())
class UserOrder:
    # username: auto
    ethereum_address: auto
    # email: auto
    funds: FundOrder


# types
@strawberry.django.type(models.Price)
class Price:
    id: auto
    date: auto
    gav: auto
    nav_per_share: auto
    fund: "Fund"


@strawberry.django.type(models.Fund)
class Fund:
    vault_proxy: auto
    comptroller_proxy: auto
    name: auto
    description: auto
    denominated_asset: "Asset"
    creator: auto
    depositors: auto
    price: List["Price"]


@strawberry.django.type(models.Asset)
class Asset:
    address: auto
    name: auto
    funds: List["Fund"]


@strawberry_django.type(get_user_model())
class User:
    # id: auto
    # username: auto
    ethereum_address: auto
    # password: auto
    # email: auto
    funds: List["Fund"]


# input types
@strawberry_django.input(models.Fund)
class FundInput:
    vault_proxy: auto
    comptroller_proxy: auto
    name: auto
    description: auto
    denominated_asset: auto
    creator: auto
    depositors: auto


@strawberry.django.input(models.Asset)
class AssetInput:
    address: auto
    name: auto


@strawberry_django.input(get_user_model())
class UserInput:
    # username: auto
    ethereum_address: auto
    # password: auto
    # email: auto


# partial input types
@strawberry_django.input(models.Fund, partial=True)
class FundPartialInput(FundInput):
    pass


@strawberry_django.input(models.Asset, partial=True)
class AssetPartialInput(AssetInput):
    pass
