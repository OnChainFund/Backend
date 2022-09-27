# schema.py
import strawberry
from typing import List

import strawberry_django
import strawberry_django.auth as auth
from strawberry_django import mutations
from .types import (
    Fund,
    Asset,
    FundInput,
    FundPartialInput,
    AssetInput,
    AssetPartialInput,
    User,
    UserInput,
)


@strawberry.type
class Query:
    user: User = strawberry_django.field()
    users: List[User] = strawberry_django.field()
    fund: Fund = strawberry_django.field()
    funds: List[Fund] = strawberry_django.field()
    asset: Asset = strawberry_django.field()
    assets: List[Asset] = strawberry_django.field()
    # prices: List[FundPrice] = strawberry_django.field()


@strawberry.type
class Mutation:
    createFund: Fund = mutations.create(FundInput)
    createFunds: List[Fund] = mutations.create(FundInput)
    updateFunds: List[Fund] = mutations.update(FundPartialInput)
    deleteFunds: List[Fund] = mutations.delete()

    createAsset: Asset = mutations.create(AssetInput)
    createAssets: List[Asset] = mutations.create(AssetInput)
    updateAssets: List[Asset] = mutations.update(AssetPartialInput)
    deleteAssets: List[Asset] = mutations.delete()

    register: User = auth.register(UserInput)


schema = strawberry.Schema(query=Query, mutation=Mutation)
