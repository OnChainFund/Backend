# schema.py
import strawberry
from typing import List
from .types import Price, Fund, Asset


@strawberry.type
class Query:
    allFunds: List[Fund] = strawberry.django.field()
    allAssets: List[Asset] = strawberry.django.field()
    allPrices: List[Price] = strawberry.django.field()


schema = strawberry.Schema(query=Query)
