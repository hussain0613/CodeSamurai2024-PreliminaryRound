from pydantic import BaseModel
from typing import Optional

class WalletUser(BaseModel):
        user_id: Optional[int] = None
        user_name: Optional[str] = None


class WalletBase(BaseModel):
    wallet_id: Optional[int] = None
    wallet_balance: Optional[float] = None
    
    user: Optional[WalletUser] = WalletUser()


class WalletRecharge(BaseModel):
    recharge: int
