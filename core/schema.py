import graphene
from graphene import ObjectType, Schema

from fund.schemas.schema import Query, Mutation


class Query(Query, ObjectType):  # Add your Query objects here
    pass


class Mutation(Mutation, ObjectType):  # Add your Mutation objects here
    pass


schema = Schema(query=Query, mutation=Mutation)
