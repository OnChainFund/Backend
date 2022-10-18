from django.contrib import admin

from management.forms import PriceManagementForm, StrategyForm
from .models import PriceManagement, Strategy, Weight
from import_export.admin import ImportExportModelAdmin, ImportExportMixin


class PriceManagementAdmin(ImportExportModelAdmin):
    list_display = (
        "target_asset",
        "ftx_pair_name",
        "denominated_asset",
        "update_asset_price_db",
        "update_asset_price_pangolin",
        "update_asset_price_mock_v3_aggregator",
        "is_short_position",
        "round_time",
        "schedual",
    )
    readonly_fields = [
        "schedual",
    ]
    form = PriceManagementForm


@admin.register(Strategy)
class StrategyAdmin(ImportExportModelAdmin):
    list_display = ("name", "description", "assets_count")

    form = StrategyForm


class WeightAdmin(ImportExportModelAdmin):
    list_display = ("time",)


admin.site.register(PriceManagement, PriceManagementAdmin)
# admin.site.register(WeightAdmin, Weight)
