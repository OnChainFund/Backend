import graphene
from graphene_django import DjangoObjectType
from .models import Fund


class FundType(DjangoObjectType):
    class Meta:
        model = Fund
        fields = "__all__"


class Query(graphene.ObjectType):
    all_funds = graphene.List(FundType)
    fund = graphene.Field(FundType, comptroller_proxy=graphene.String())

    def resolve_all_funds(root, info):
        return Fund.objects.all()

    def resolve_fund(self, info, comptroller_proxy):
        return Fund.objects.get(comptroller_proxy=comptroller_proxy)


class FundInput(graphene.InputObjectType):
    comptroller_proxy = graphene.String()
    vault_proxy = graphene.String()
    denominated_asset = graphene.String()
    creator = graphene.String()
    name = graphene.String()


class CreateFund(graphene.Mutation):
    class Arguments:
        fund_data = FundInput(required=True)

    fund = graphene.Field(FundType)

    @staticmethod
    def mutate(root, info, fund_data=None):
        fund_instance = Fund(
            comptroller_proxy=fund_data.comptroller_proxy,
            vault_proxy=fund_data.vault_proxy,
            denominated_asset=fund_data.denominated_asset,
            creator=fund_data.creator,
            name=fund_data.name,
        )
        fund_instance.save()
        return CreateFund(fund=fund_instance)


class UpdateFund(graphene.Mutation):
    class Arguments:
        fund_data = FundInput(required=True)

    fund = graphene.Field(FundType)

    @staticmethod
    def mutate(root, info, fund_data=None):

        fund_instance = Fund.objects.get(pk=fund_data.comptroller_proxy)

        if fund_instance:
            fund_instance.vault_proxy = (fund_data.vault_proxy,)
            fund_instance.denominated_asset = (fund_data.denominated_asset,)
            fund_instance.creator = (fund_data.creator,)
            fund_instance.name = (fund_data.name,)
            fund_instance.save()

            return UpdateFund(fund=fund_instance)
        return UpdateFund(fund=None)


class DeleteFund(graphene.Mutation):
    class Arguments:
        comptroller_proxy = graphene.String()

    fund = graphene.Field(FundType)

    @staticmethod
    def mutate(root, info, comptroller_proxy):
        fund_instance = Fund.objects.get(pk=comptroller_proxy)
        fund_instance.delete()
        return None


class Mutation(graphene.ObjectType):
    create_fund = CreateFund.Field()
    update_fund = UpdateFund.Field()
    delete_fund = DeleteFund.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
