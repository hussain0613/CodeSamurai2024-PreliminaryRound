from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from app.db_utils import Base

class Train(Base):
    __tablename__ = "train"
    
    train_id: Mapped[int] = mapped_column(primary_key=True)
    train_name: Mapped[str]
    capacity: Mapped[int]


class Stops(Base):
    __tablename__ = "stop"

    stop_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    
    train_id: Mapped[int] = mapped_column(ForeignKey("train.train_id"))
    station_id: Mapped[int] = mapped_column(ForeignKey("station.station_id"))
    
    arrival_time: Mapped[str] = mapped_column(nullable=True)
    departure_time: Mapped[str] = mapped_column(nullable=True)
    fare: Mapped[int] 

    
