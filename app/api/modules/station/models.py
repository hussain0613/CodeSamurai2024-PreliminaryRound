from sqlalchemy.orm import Mapped, mapped_column
from app.db_utils import Base

class Station(Base):
    __tablename__ = "station"
    
    station_id: Mapped[int] = mapped_column(primary_key=True)
    station_name: Mapped[str]
    longitude: Mapped[float]
    latitude: Mapped[float]
