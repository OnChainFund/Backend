from random import random
from django.utils import timezone
from django.db import models
from django.forms import ValidationError
from django.utils.functional import lazy as _
from django_q.models import Schedule
from fund.models import Asset
from utils.constants import FTX_TRADING_PAIR_LIST
from utils.utils import args_to_string
from .fields import CustomDurationField
from django.utils.translation import gettext_lazy as _
from django_jsonform.models.fields import JSONField
from django.conf import settings
import datetime


class PriceManagement(models.Model):
    ftx_pair_name = models.CharField(max_length=100, null=True, blank=True)

    target_asset = models.ForeignKey(
        to=Asset,
        verbose_name="資產",
        on_delete=models.CASCADE,
        null=False,
        related_name="target_asset",
    )
    denominated_asset = models.ForeignKey(
        to=Asset,
        verbose_name="對價資產",
        on_delete=models.CASCADE,
        null=False,
        related_name="denominated_asset",
    )
    pangolin_pool_address = models.CharField(max_length=255, null=True, blank=True)
    # round_time = models.DurationField(null=True)
    round_time = CustomDurationField(null=True)
    round_start_time = models.DateTimeField(null=True)
    update_asset_price_db = models.BooleanField(default=False)
    update_asset_price_pangolin = models.BooleanField(default=False)
    update_asset_price_mock_v3_aggregator = models.BooleanField(default=False)
    is_short_position = models.BooleanField(default=False)
    schedual = models.OneToOneField(
        Schedule,
        on_delete=models.SET_NULL,
        null=True,
        related_name="schedual",
    )

    def __str__(self):
        return self.target_asset.name + "/" + self.denominated_asset.name


class Strategy(models.Model):
    class StrategyStatus(models.TextChoices):
        RUNNING = "RUN", _("Running")
        PAUSED = "PAUSE", _("Paused")

    title = models.TextField(verbose_name="標題", null=True, blank=True)
    description = models.TextField(verbose_name="簡介", null=True, blank=True)
    creator = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True
    )
    status = models.CharField(
        max_length=10, choices=StrategyStatus.choices, default=StrategyStatus.PAUSED
    )
    assets = models.ManyToManyField(to=Asset)
    model = models.FileField()


class Weight(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    WEIGHTS_SCHEMA = {
        "type": "array",
        "weight": {
            "asset": "integer",
            "ratio": "integer",
        },
    }

    weights = JSONField(schema=WEIGHTS_SCHEMA)
    strategy = models.ForeignKey(
        to=Strategy, related_name="weights", on_delete=models.CASCADE
    )
    buffer = models.IntegerField()

    def __str__(self):
        return self.strategy.title + ":" + str(self.time)

    class Meta:
        unique_together = (("time", "strategy"),)
