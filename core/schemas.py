from django.conf import settings
from fund.schemas import Query as FundQuery, Mutation as FundMutation

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


schema = strawberry.Schema(query=Query, mutation=Mutation)
