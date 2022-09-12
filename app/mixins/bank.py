from app.services.bank import BankService
from typing import Any
from injector import inject


class BankServiceMixins:
    @inject
    def __init__(self,  bank_service: BankService ,**kwargs: Any) -> None:
        self.bank_service = bank_service
        super().__init__(**kwargs)