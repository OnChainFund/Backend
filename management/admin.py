from django.contrib import admin

from management.forms import LiquidityManagementForm, StrategyForm
from .models import LiquidityManagement, Strategy, Weight
from import_export.admin import ImportExportModelAdmin, ImportExportMixin


class LiquidityManagementAdmin(ImportExportModelAdmin):
    list_display = (
        "ftx_pair_name",
        "target_asset",
        "denominated_asset",
        # "schedual",
        "round_time",
    )
    readonly_fields = [
        "schedual",
    ]
    form = LiquidityManagementForm


class StrategyAdmin(ImportExportModelAdmin):
    list_display = (
        "title",
        "description",
    )
    form = StrategyForm


class WeightAdmin(ImportExportModelAdmin):
    list_display = ("time",)


admin.site.register(LiquidityManagement, LiquidityManagementAdmin)
admin.site.register(Strategy, StrategyAdmin)
# admin.site.register(WeightAdmin, Weight)
