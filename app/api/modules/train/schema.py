from pydantic import BaseModel
from typing import Optional

class TrainStopsBase(BaseModel):
    station_id: int
    
    arrival_time: Optional[str] = None
    departure_time: str | None = None
    
    fare: int


class TrainCreate(BaseModel):
    train_id: int
    train_name: str
    capacity: int

    stops: list[TrainStopsBase] = []



class TrainCreateResponse(BaseModel):
    train_id: int
    train_name: str
    capacity: int

    service_start: str = None
    service_end: str = None

    num_stations: int = None
