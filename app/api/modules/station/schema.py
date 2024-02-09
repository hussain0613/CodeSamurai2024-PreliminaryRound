from pydantic import BaseModel

class StationBase(BaseModel):
    station_id: int
    station_name: str
    longitude: float
    latitude: float

    class Config:
        from_attributes = True

class StationsResponse(BaseModel):
    stations: list[StationBase]


class StationTrainResponse(BaseModel):
    station_id: int

    class Train(BaseModel):
        train_id: int
        arrival_time: str | None = None
        departure_time: str | None = None
    
    trains: list[Train] = []