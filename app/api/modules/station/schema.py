from pydantic import BaseModel

class StationBase(BaseModel):
    station_id: int
    station_name: str
    longitude: float
    latitude: float

    class Config:
        from_attributes = True
