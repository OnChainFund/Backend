from django.db import models
from django.forms import ValidationError
from django.utils.functional import lazy as _
from django_q.models import Schedule
from fund.models import Asset
from utils.constants import FTX_TRADING_PAIR_LIST
from .fields import CustomDurationField


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
            args=[self.target_asset, self.denominated_asset, self.ftx_pair_name],
            schedule_type=Schedule.DAILY,
        )
        super(LiquidityManagement, self).save(*args, **kwargs)
