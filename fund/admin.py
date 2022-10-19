from django.contrib import admin
from .models import AssetPrice, Fund, Asset, FundPrice, Wallet
from import_export.admin import ImportExportModelAdmin, ImportExportMixin
from import_export import resources


class AssetResource(resources.ModelResource):
    model = Asset
    # skip_unchanged = True
    # report_skipped = True
    exclude = ("id",)


# import_id_fields = ("address",)
# fields = (
#     "address",
#     "name",
#     "price_feed",
#     "price_feed_is_mocked",
#     "ftx_pair_name",
#     "is_short_position",
# )


class AssetAdmin(ImportExportModelAdmin):
    resource_class = AssetResource
    fields = [
        "address",
        "name",
        "price_feed",
        "price_feed_is_mocked",
        "ftx_pair_name",
        "is_short_position",
    ]
    list_display = ("name", "address", "price_feed_is_mocked")


class FundAdmin(ImportExportModelAdmin):
    list_display = (
        "name",
        "symbol",
        "vault_proxy",
        "denominated_asset",
        "comptroller_proxy",
        "creator",
    )


class FundPriceAdmin(ImportExportModelAdmin):
    list_display = ("fund", "time", "gav", "nav_per_share")
    list_filter = ("fund",)


class AssetPriceAdmin(ImportExportModelAdmin):
    list_display = ("asset", "time", "price")
    list_filter = ("asset",)


class WalletAdmin(ImportExportModelAdmin):
    list_display = ("address",)


class StrategyAdmin(ImportExportModelAdmin):
    list_display = (
        "name",
        "creator",
    )


admin.site.register(Asset, AssetAdmin)
admin.site.register(Fund, FundAdmin)
admin.site.register(FundPrice, FundPriceAdmin)
admin.site.register(AssetPrice, AssetPriceAdmin)
admin.site.register(Wallet, WalletAdmin)
