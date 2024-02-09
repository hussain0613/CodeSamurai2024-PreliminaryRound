from typing import Literal

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse


from sqlalchemy.orm import Session
from app.db_utils import engine


from .schema import *

from app.api.modules.user.models import User

router = APIRouter(prefix="/wallets", tags=["wallets"])


@router.get("/{wallet_id}")
def get_wallet(wallet_id: int) -> WalletBase:
    with Session(engine) as session:
        user: User = session.query(User).get(wallet_id)
        if not user:
            msg_dict = {"message": f"wallet with id: {wallet_id} was not found"}
            return JSONResponse(msg_dict, status_code=404)
        
        wallet_response: WalletBase = WalletBase()

        wallet_response.wallet_id = user.user_id
        wallet_response.wallet_balance = user.balance
        wallet_response.user.user_id = user.user_id
        wallet_response.user.user_name = user.user_name


        return wallet_response


@router.put("/{wallet_id}")
def recharge_wallet(recharge: WalletRecharge, wallet_id):

    with Session(engine) as session:
        user: User = session.query(User).get(wallet_id)
        if not user:
            msg_dict = {"message": f"wallet with id: {wallet_id} was not found"}
            return JSONResponse(msg_dict, status_code=404)
        
        if recharge.recharge < 100 or recharge.recharge > 10000:
            msg_dict = {"message": f"invalid amount: {recharge.recharge}"}
            return JSONResponse(msg_dict, status_code=400)
        
        user.balance += recharge.recharge
        session.commit()
        
        wallet_response: WalletBase = WalletBase()

        wallet_response.wallet_id = user.user_id
        wallet_response.wallet_balance = user.balance
        wallet_response.user.user_id = user.user_id
        wallet_response.user.user_name = user.user_name


        return wallet_response
