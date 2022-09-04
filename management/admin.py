from django.contrib import admin

from management.forms import LiquidityManagementForm
from .models import LiquidityManagement
from import_export.admin import ImportExportModelAdmin, ImportExportMixin


class LiquidityManagementAdmin(ImportExportModelAdmin):
    list_display = (
        "ftx_pair_name",
        "target_asset",
        "denominated_asset",
        "schedual",
        "round_time",
    )
    form = LiquidityManagementForm


admin.site.register(LiquidityManagement, LiquidityManagementAdmin)
