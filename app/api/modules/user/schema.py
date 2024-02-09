from pydantic import BaseModel

class UserBase(BaseModel):
    user_id: int
    user_name: str
    balance: int

    class Config:
        from_attributes = True
