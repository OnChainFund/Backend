# cookbook/ingredients/models.py
from tkinter import CASCADE
from django.db import models
from django.utils import timezone
from django.conf import settings


class Asset(models.Model):
    address = models.CharField(max_length=100, unique=True, primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    price_feed = models.CharField(max_length=100, null=True)
    price_feed_is_mocked = models.BooleanField(default=False)

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
    description = models.TextField(verbose_name="基金簡介", null=True, blank=True)
    creator = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        related_name="created_funds",
        verbose_name="創建者",
        on_delete=models.CASCADE,
    )
    denominated_asset = models.ForeignKey(
        to=Asset,
        verbose_name="定價資產",
        on_delete=models.CASCADE,
        null=False,
        related_name="funds",
    )
    depositors = models.ManyToManyField(
        to=settings.AUTH_USER_MODEL, related_name="invested_funds", verbose_name="投資者"
    )
    # depositor = models.ForeignKey
    class Meta:
        get_latest_by = "name"

    def __str__(self):
        return self.name


class FundPrice(models.Model):
    date = models.DateField(auto_now_add=True)
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
        return self.fund.name + ":" + str(self.date)

    class Meta:
        unique_together = (("date", "fund"),)
