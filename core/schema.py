import graphene

from fund.schema import Query, Mutation


class Query(Query, graphene.ObjectType):  # Add your Query objects here
    pass


class Mutation(Mutation, graphene.ObjectType):  # Add your Mutation objects here
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
