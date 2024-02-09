from sqlalchemy.orm import Mapped, mapped_column
from app.db_utils import Base

class User(Base):
    __tablename__ = "user"
    
    user_id: Mapped[int] = mapped_column(primary_key=True)
    user_name: Mapped[str]
    balance: Mapped[int]
