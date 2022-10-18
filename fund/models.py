from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class Asset(models.Model):
    address = models.CharField(
        max_length=100, verbose_name="地址", primary_key=True, unique=True
    )
    name = models.CharField(max_length=100, unique=True)
    price_feed = models.CharField(max_length=100, null=True)
    price_feed_is_mocked = models.BooleanField(default=False)
    ftx_pair_name = models.CharField(max_length=100, null=True)
    is_short_position = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Fund(models.Model):
    # id = models.CharField(_(""), max_length=50)
    vault_proxy = models.CharField(
        max_length=100, verbose_name="金庫代理", primary_key=True, unique=True
    )
    comptroller_proxy = models.CharField(
        max_length=100, unique=True, verbose_name="控制器代理"
    )

    name = models.CharField(max_length=100, null=True, verbose_name="基金名稱", blank=True)

    symbol = models.CharField(
        max_length=100, null=True, verbose_name="基金代幣名稱", blank=True
    )
    description = models.TextField(verbose_name="基金簡介", null=True, blank=True)
    detail = models.TextField(verbose_name="基金詳細介紹", null=True, blank=True)
    creator = models.CharField(
        max_length=100, null=True, verbose_name="創建者", blank=True
    )
    denominated_asset = models.CharField(
        max_length=100, null=True, verbose_name="定價資產", blank=True
    )
    subscribed_strategy = models.ForeignKey(
        "management.Strategy",
        verbose_name="訂閱策略",
        on_delete=models.SET_NULL,
        null=True,
        related_name="funds",
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        get_latest_by = "name"

    def __str__(self):
        return self.name


class FundPrice(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    gav = models.FloatField(default=0)
    nav_per_share = models.FloatField(default=0)
    fund = models.ForeignKey(
        to=Fund,
        verbose_name="基金",
        on_delete=models.CASCADE,
        null=False,
        related_name="price",
    )

    def __str__(self):
        return self.fund.comptroller_proxy + ":" + str(self.time)

    class Meta:
        unique_together = (("time", "fund"),)


class AssetPrice(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    price = models.FloatField()
    asset = models.ForeignKey(
        to=Asset,
        verbose_name="資產",
        on_delete=models.CASCADE,
        null=False,
        related_name="price",
    )

    def __str__(self):
        return self.asset.name + ":" + str(self.time)

    class Meta:
        unique_together = (("time", "asset"),)


class Wallet(models.Model):
    address = models.CharField(
        max_length=100, verbose_name="地址", primary_key=True, unique=True
    )
    invested_funds = models.ManyToManyField(Fund, related_name="depositors")
