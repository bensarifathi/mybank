from django.db import models
from .abstract import SoftDelete, Timestamps
from django.contrib.auth.models import User


class Bank(SoftDelete, Timestamps):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=25, decimal_places=2)

    def __str__(self) -> str:
        return f'{self.user}-{self.amount} DZD'