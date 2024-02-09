from typing import List, Optional

from pydantic import BaseModel


class UserCreate(BaseModel):
    user_id: int
    user_name: str
    balance: int


class UserBase(UserCreate):
    user_id: int
    user_name: str
    balance: int

    class Config:
        from_attributes = True

class UserListResponse(BaseModel):
    users: List[UserBase]