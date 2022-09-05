from django.contrib import admin
from .models import Fund, Asset
from import_export.admin import ImportExportModelAdmin, ImportExportMixin


class AssetAdmin(ImportExportModelAdmin):
    list_display = (
        "name",
        "comptroller_proxy",
        "vault_proxy",
        "creator",
        "denominated_asset",
    )


class FundAdmin(ImportExportModelAdmin):
    pass


admin.site.register(Asset, AssetAdmin)
admin.site.register(Fund, FundAdmin)
