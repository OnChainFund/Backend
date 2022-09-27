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

    # round_time = models.DurationField(null=True)
    round_time = CustomDurationField(null=True)
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

    def save(self, *args, **kwargs):
        # test if ftx has the trading pair
        if self.ftx_pair_name not in FTX_TRADING_PAIR_LIST:
            raise ValidationError(
                _("Invalid input of ftx trading pair: %(value)s"),
                code="invalid",
                params={"value": self.ftx_pair_name},
            )
        # remove last schedual
        if self.schedual:
            self.schedual.delete()

        # set variable (can be better)
        if self.update_asset_price_db:
            self.update_asset_price_db = True
        else:
            self.update_asset_price_db = False
        if self.update_asset_price_pangolin:
            self.update_asset_price_pangolin = True
        else:
            self.update_asset_price_pangolin = False
        if self.update_asset_price_mock_v3_aggregator:
            self.update_asset_price_mock_v3_aggregator = True
        else:
            self.update_asset_price_mock_v3_aggregator = False

        if self.update_asset_price_mock_v3_aggregator:
            if not self.target_asset.price_feed_is_mocked:

                raise ValidationError(
                    _("The Price Feed is in Oracle, can't be change by user"),
                    code="invalid",
                    params={"value": self.ftx_pair_name},
                )

            if not self.target_asset.price_feed:
                raise ValidationError(
                    _("The price feed of target asset DoesNotExist"),
                    code="invalid",
                    params={"value": self.ftx_pair_name},
                )

        self.schedual = Schedule.objects.create(
            func="management.tasks.manage_price",
            name="PM:" + self.target_asset.name,
            repeats=-1,
            args=args_to_string(
                [
                    self.target_asset.address,
                    self.denominated_asset.address,
                    self.ftx_pair_name,
                    self.target_asset.price_feed,
                    self.update_asset_price_db,
                    self.update_asset_price_pangolin,
                    self.update_asset_price_mock_v3_aggregator,
                    self.is_short_position,
                ]
            ),
            schedule_type=Schedule.HOURLY,
        )
        super(PriceManagement, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.schedual:
            self.schedual.delete()
        return super(PriceManagement, self).delete(*args, **kwargs)


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
