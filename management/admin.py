from django.contrib import admin

from management.forms import PriceManagementForm, StrategyForm
from .models import PriceManagement, Strategy, Weight
from import_export.admin import ImportExportModelAdmin, ImportExportMixin


class PriceManagementAdmin(ImportExportModelAdmin):
    list_display = (
        "ftx_pair_name",
        "target_asset",
        "denominated_asset",
        # "schedual",
        "round_time",
        "update_price_pangolin",
        "update_price_mock_v3_aggregator",
    )
    readonly_fields = [
        "update_price_pangolin_schedual",
        "update_price_mock_v3_aggregator_schedual",
    ]
    form = PriceManagementForm


class StrategyAdmin(ImportExportModelAdmin):
    list_display = (
        "title",
        "description",
    )
    form = StrategyForm


class WeightAdmin(ImportExportModelAdmin):
    list_display = ("time",)


admin.site.register(PriceManagement, PriceManagementAdmin)
admin.site.register(Strategy, StrategyAdmin)
# admin.site.register(WeightAdmin, Weight)
