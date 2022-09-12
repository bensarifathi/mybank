from django.contrib import admin
from app.models.bank import Bank
from app.models.wallet import Wallet
from app.models.mouvement import Mouvement


admin.site.register(Bank)
admin.site.register(Wallet)
admin.site.register(Mouvement)