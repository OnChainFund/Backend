from django.contrib.auth.models import AbstractUser
from django.db import models

from .managers import Web3UserManager


class User(AbstractUser):
    email = models.EmailField(("email address"), unique=True)
    address_verified = models.BooleanField(default=False)
    address = models.CharField(max_length=255, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = Web3UserManager()

    def __str__(self):
        return self.email

    class Meta:
        db_table = "auth_user"
