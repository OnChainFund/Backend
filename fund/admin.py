from django.contrib import admin
from .models import Fund, Asset
from import_export.admin import ImportExportModelAdmin, ImportExportMixin


class AssetAdmin(ImportExportModelAdmin):
    list_display = (
        "name",
        "address",
    )


class FundAdmin(ImportExportModelAdmin):
    pass


admin.site.register(Asset, AssetAdmin)
admin.site.register(Fund, FundAdmin)
