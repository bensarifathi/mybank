from django.db import models
from .abstract import SoftDelete, Timestamps
from django.contrib.auth.models import User


class Mouvement(SoftDelete, Timestamps):
    BANK = 0
    WALLET = 1

    CHOICE = (
        (BANK, 'Bank'),
        (WALLET, 'Wallet')
    )

    IN = 0
    OUT = 1

    TYPE = (
        (IN, 'IN'),
        (OUT, 'OUT')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    entity = models.PositiveIntegerField(choices=CHOICE)
    direction = models.PositiveIntegerField(choices=TYPE)
    amount = models.DecimalField(max_digits=25, decimal_places=3)

    def __str__(self) -> str:
        return f"{self.direction}-{self.entity}"