# cookbook/ingredients/models.py
from django.db import models
from django.utils import timezone


class Asset(models.Model):
    address = models.CharField(max_length=100, unique=True, primary_key=True)
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Fund(models.Model):
    # id = models.CharField(_(""), max_length=50)
    comptroller_proxy = models.CharField(
        max_length=100, unique=True, verbose_name="控制器代理", primary_key=True
    )
    vault_proxy = models.CharField(max_length=100, verbose_name="金庫代理", unique=True)
    name = models.CharField(max_length=100, null=True, verbose_name="基金名稱", blank=True)
    creator = models.CharField(
        max_length=100, null=True, verbose_name="創建者", blank=True
    )
    denominated_asset = models.ForeignKey(
        to=Asset,
        verbose_name="定價資產",
        on_delete=models.CASCADE,
        null=False,
        related_name="funds",
    )
    depositors = models.PositiveIntegerField(verbose_name="投資者", default=0)

    def __str__(self):
        return self.name


class Price(models.Model):
    date = models.DateField(auto_now_add=True)
    fund = models.ForeignKey(
        to=Fund,
        verbose_name="基金",
        on_delete=models.CASCADE,
        null=False,
        related_name="price",
    )

    def __str__(self):
        return self.fund.name + ":" + self.date
