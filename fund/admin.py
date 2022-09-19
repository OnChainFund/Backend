from django.contrib import admin
from .models import Fund, Asset, Price
from import_export.admin import ImportExportModelAdmin, ImportExportMixin


class AssetAdmin(ImportExportModelAdmin):
    list_display = (
        "name",
        "address",
    )


class FundAdmin(ImportExportModelAdmin):
    list_display = (
        "name",
        "denominated_asset",
        "comptroller_proxy",
        "vault_proxy",
        "creator",
        # "depositors",
    )


class PriceAdmin(ImportExportModelAdmin):
    list_display = ("date", "fund", "gav", "nav_per_share")


admin.site.register(Asset, AssetAdmin)
admin.site.register(Fund, FundAdmin)
admin.site.register(Price, PriceAdmin)
