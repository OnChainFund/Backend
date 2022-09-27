from django.contrib import admin
from .models import Fund, Asset, FundPrice
from import_export.admin import ImportExportModelAdmin, ImportExportMixin


class AssetAdmin(ImportExportModelAdmin):
    list_display = ("name", "address", "price_feed_is_mocked")


class FundAdmin(ImportExportModelAdmin):
    list_display = (
        "name",
        "denominated_asset",
        # "comptroller_proxy",
        # "vault_proxy",
        # "creator",
        # "depositors",
    )


class FundPriceAdmin(ImportExportModelAdmin):
    list_display = ("date", "fund", "gav", "nav_per_share")


admin.site.register(Asset, AssetAdmin)
admin.site.register(Fund, FundAdmin)
admin.site.register(FundPrice, FundPriceAdmin)
