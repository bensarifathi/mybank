from app.services.mouvement import MouvementService
from typing import Any
from injector import inject


class MouvementServiceMixins:
    @inject
    def __init__(self,  mouvement_service: MouvementService ,**kwargs: Any) -> None:
        self.mouvement_service = mouvement_service
        super().__init__(**kwargs)