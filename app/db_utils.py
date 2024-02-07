from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import create_engine

class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, nullable=False, unique=True, name="id", doc="This is the default primary key for every model.")

engine = create_engine("sqlite:///./app.db")

