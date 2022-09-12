from app.models.bank import Bank
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404


class BankService:

    def get_all(self) -> QuerySet[Bank]:
        return Bank.objects.all()
        
    def get_by_id(self, id: int) -> Bank:
        return get_object_or_404(Bank, pk=id)
    
    def create(self, **kwargs) -> Bank:
        return Bank.objects.create(**kwargs)

    def update(self, id: int, **kwargs) -> Bank:
        bank = self.get_by_id(id)
        for k, v in kwargs.items():
            setattr(bank, k, v)
        bank.save()
        return bank
    
    def delete(self, id: int) -> None:
        bank = self.get_by_id(id)
        bank.delete()