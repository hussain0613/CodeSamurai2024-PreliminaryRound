from typing import Literal

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse


from sqlalchemy.orm import Session
from app.db_utils import engine


from .models import *
from .schema import *

from app.api.modules.train.models import Stops

router = APIRouter(prefix="/stations", tags=["stations"])

@router.post("/", status_code=201)
def create_station(station: StationBase) -> StationBase:
    with Session(engine) as session:
        station_db = Station(**station.model_dump(exclude_unset=True))
        session.add(station_db)
        session.commit()
        session.refresh(station_db)
        station_response: StationBase = StationBase.model_validate(station_db)
        
    return station_response

@router.get("/")
def get_stations() -> StationsResponse:
    with Session(engine) as session:
        stations = session.query(Station).all()
        stations_response: list[StationBase] = [StationBase.model_validate(station, from_attributes=True) for station in stations]
        return StationsResponse(stations=stations_response)



@router.get("/{station_id}/trains", tags=["stations", "trains"])
def get_trains(station_id: int) -> StationTrainResponse:
    with Session(engine) as session:
        station = session.query(Station).get(station_id)
        if not station:
            msg_dict = {"message": f"station with id: {station_id} was not found"}
            return JSONResponse(msg_dict, status_code=404)
        
        trains = session.query(Stops).filter(Stops.station_id == station_id).all()
        trains_response: list[StationTrainResponse.Train] = [StationTrainResponse.Train.model_validate(train, from_attributes=True) for train in trains]

        return StationTrainResponse(station_id=station_id, trains=trains_response)

