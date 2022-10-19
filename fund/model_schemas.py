from djantic.main import ModelSchema
from fund.models import Asset


class AssetSchema(ModelSchema):
    class Config:
        model = Asset
        include = [
            "name",
            "address",
            "ftx_pair_name",
            "is_short_position",
            "price_feed",
            "price_feed_is_mocked",
        ]
