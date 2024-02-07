from sqlalchemy.orm import Mapped
from app.db_utils import Base

class Book(Base):
    __tablename__ = "books"
    
    title: Mapped[str]
    author: Mapped[str]
    genre: Mapped[str]
    price: Mapped[float]
