from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404
from app.models.wallet import Wallet


class WalletService:

    def get_all(self) -> QuerySet[Wallet]:
        return Wallet.objects.all()
        
    def get_by_id(self, id: int) -> Wallet:
        return get_object_or_404(Wallet, pk=id)
    
    def create(self, **kwargs) -> Wallet:
        return Wallet.objects.create(**kwargs)

    def update(self, id: int, **kwargs) -> Wallet:
        wallet = self.get_by_id(id)
        for k, v in kwargs.items():
            setattr(wallet, k, v)
        wallet.save()
        return wallet
    
    def delete(self, id: int) -> None:
        wallet = self.get_by_id(id)
        wallet.delete()