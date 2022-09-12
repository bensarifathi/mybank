from app.services.wallet import WalletService
from typing import Any
from injector import inject


class WalletServiceMixins:
    @inject
    def __init__(self,  wallet_service: WalletService ,**kwargs: Any) -> None:
        self.wallet_service = wallet_service
        super().__init__(**kwargs)