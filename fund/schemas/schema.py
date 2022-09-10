from graphene import (
    relay,
    ObjectType,
    Field,
    List,
    String,
    InputObjectType,
    Schema,
    Mutation,
)
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from ..models import Asset, Fund, Price


class AssetNode(DjangoObjectType):
    class Meta:
        model = Asset
        fields = "__all__"
        # interfaces = (relay.Node,)


class PriceNode(DjangoObjectType):
    class Meta:
        model = Price
        fields = "__all__"


class FundNode(DjangoObjectType):
    class Meta:
        model = Fund
        fields = (
            "name",
            "comptroller_proxy",
            "vault_proxy",
            "denominated_asset",
            "creator",
            "price",
            "depositors",
        )
        # filter_fields = {
        #     "name": ["istartswith"],
        #     "comptroller_proxy": ["exact"],
        #     "denominated_asset": ["exact"],
        #     "creator": ["exact"],
        # }
        # interfaces = (relay.Node,)


class Query(ObjectType):
    # asset = relay.Node.Field(AssetNode)
    asset = Field(AssetNode, address=String())
    all_assets = List(AssetNode)
    price = Field(PriceNode, address=String())
    all_prices = List(PriceNode)
    fund = Field(FundNode, vault_proxy=String())
    all_funds = List(FundNode)

    def resolve_all_assets(root, info):
        return Asset.objects.all()

    def resolve_asset(self, info, address):
        return Asset.objects.get(address=address)

    def resolve_all_prices(root, info):
        return Price.objects.all()

    def resolve_price(self, info, address):
        return Price.objects.get(address=address)

    def resolve_all_funds(root, info):
        return Fund.objects.all()

    def resolve_fund(self, info, vault_proxy):
        return Fund.objects.get(vault_proxy=vault_proxy)


class FundInput(InputObjectType):
    comptroller_proxy = String()
    vault_proxy = String()
    denominated_asset = String()
    creator = String()
    name = String()


class CreateFund(Mutation):
    class Arguments:
        fund_data = FundInput(required=True)

    fund = Field(FundNode)

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


class UpdateFund(Mutation):
    class Arguments:
        fund_data = FundInput(required=True)

    fund = Field(FundNode)

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


class DeleteFund(Mutation):
    class Arguments:
        comptroller_proxy = String()

    fund = Field(FundNode)

    @staticmethod
    def mutate(root, info, comptroller_proxy):
        fund_instance = Fund.objects.get(pk=comptroller_proxy)
        fund_instance.delete()
        return None


class Mutation(ObjectType):
    create_fund = CreateFund.Field()
    update_fund = UpdateFund.Field()
    delete_fund = DeleteFund.Field()


schema = Schema(query=Query, mutation=Mutation)
