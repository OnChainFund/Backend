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
from users.models import User


class LiquidityManagement(models.Model):
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
    schedual = models.OneToOneField(Schedule, on_delete=models.CASCADE, null=True)
    # round_time = models.DurationField(null=True)
    round_time = CustomDurationField(null=True)

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
        self.schedual = Schedule.objects.create(
            func="management.tasks.manage_liquidity",
            name="LM:" + self.ftx_pair_name,
            repeats=-1,
            args=args_to_string(
                [
                    self.target_asset.address,
                    self.denominated_asset.address,
                    self.ftx_pair_name,
                ]
            ),
            schedule_type=Schedule.HOURLY,
        )
        super(LiquidityManagement, self).save(*args, **kwargs)


class Strategy(models.Model):
    class StrategyStatus(models.TextChoices):
        RUNNING = "RUN", _("Running")
        PAUSED = "PAUSE", _("Paused")

    title = models.TextField(verbose_name="標題", null=True, blank=True)
    description = models.TextField(verbose_name="簡介", null=True, blank=True)
    creator = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True)
    status = models.CharField(
        max_length=10, choices=StrategyStatus.choices, default=StrategyStatus.PAUSED
    )
    assets = models.ManyToManyField(to=Asset)


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
