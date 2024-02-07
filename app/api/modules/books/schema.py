from pydantic import BaseModel
from typing import List, Optional


class BookCreate(BaseModel):
    title: str
    author: str
    genre: str
    price: float


class BookUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    genre: Optional[str] = None
    price: Optional[float] = None


class Book(BookCreate):
    id: int
    title: str
    author: str
    genre: str
    price: float

    class Config:
        from_attributes = True


class BookSearch(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    genre: Optional[str] = None


class BookListResponse(BaseModel):
    books: List[Book]

