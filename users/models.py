from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from siwe_auth.models import (
    Wallet as BaseWallet,
    validate_ethereum_address,
    WalletManager as BaseWalletManager,
)


class WalletManager(BaseWalletManager):
    def create_user(self, ethereum_address: str, password=""):
        """
        Creates and saves a User with the given ethereum address.
        """
        if not ethereum_address:
            raise ValueError("Users must have an ethereum address")

        wallet = self.model()
        wallet.ethereum_address = ethereum_address
        if password != "":
            wallet.password = password

        wallet.save(using=self._db)
        return wallet

    def create_superuser(self, ethereum_address: str, password):
        """
        Creates and saves a superuser with the given ethereum address.
        """
        user = self.create_user(ethereum_address=ethereum_address, password=password)
        # user.set_unusable_password()
        user.set_password(user.password)
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Wallet(BaseWallet):
    # password = models.CharField(_("password"), max_length=128, blank=True, null=True)
    objects = WalletManager()

    USERNAME_FIELD = "ethereum_address"

    objects = WalletManager()

    def __str__(self):
        return self.ethereum_address

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
