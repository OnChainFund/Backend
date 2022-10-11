from django.conf import settings
from fund.schemas import Query as FundQuery, Mutation as FundMutation
from strawberry_django_jwt.middleware import (
    JSONWebTokenMiddleware,
)
from strawberry import Schema
import strawberry

if settings.DEBUG == True:

    class Query(FundQuery):
        pass

    class Mutation(FundMutation):
        pass

else:

    class Query(FundQuery):
        pass

    class Mutation(FundMutation):
        pass


schema = strawberry.Schema(
    query=Query,
    mutation=Mutation,
    # extensions=[
    #    JSONWebTokenMiddleware,
    #    # AsyncJSONWebTokenMiddleware,
    # ],
)
