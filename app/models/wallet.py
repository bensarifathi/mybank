from .abstract import SoftDelete, Timestamps
from django.db import models
from django.contrib.auth.models import User


class Wallet(SoftDelete, Timestamps):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(decimal_places=3, max_digits=25)

    def __str__(self) -> str:
        return f"{self.user}-{self.amount}"