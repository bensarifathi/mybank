from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404
from app.models.mouvement import Mouvement


class MouvementService:

    def get_all(self) -> QuerySet[Mouvement]:
        return Mouvement.objects.all()
        
    def get_by_id(self, id: int) -> Mouvement:
        return get_object_or_404(Mouvement, pk=id)
    
    def create(self, **kwargs) -> Mouvement:
        return Mouvement.objects.create(**kwargs)

    def update(self, id: int, **kwargs) -> Mouvement:
        mouvement = self.get_by_id(id)
        for k, v in kwargs.items():
            setattr(mouvement, k, v)
        mouvement.save()
        return mouvement
    
    def delete(self, id: int) -> None:
        mouvement = self.get_by_id(id)
        mouvement.delete()