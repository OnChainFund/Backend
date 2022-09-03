# cookbook/ingredients/models.py
from django.db import models


class Asset(models.Model):
    address = models.CharField(max_length=100, unique=True, primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.name


class Fund(models.Model):
    # id = models.CharField(_(""), max_length=50)
    comptroller_proxy = models.CharField(max_length=100, unique=True, primary_key=True)
    vault_proxy = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    creator = models.CharField(max_length=100, null=True, blank=True)
    denominated_asset = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name
