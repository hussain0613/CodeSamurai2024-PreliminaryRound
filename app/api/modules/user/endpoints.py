from typing import Literal

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from app.db_utils import engine

from .models import *
from .schema import *

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/", status_code=201)
def create_user(user: UserCreate) -> UserBase:
    """
    Creates a new user
    """
    with Session(engine) as session:
        user_db: User = User(**user.model_dump(exclude_unset=True))
        session.add(user_db)
        session.commit()
        session.refresh(user_db)
        user_response: UserBase = UserBase.model_validate(user_db)

        
    return user_response


