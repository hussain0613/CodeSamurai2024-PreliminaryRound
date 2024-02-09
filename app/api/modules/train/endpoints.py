from typing import Literal

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse


from sqlalchemy.orm import Session
from app.db_utils import engine


from .models import *
from .schema import *

router = APIRouter(prefix="/trains", tags=["trains"])

@router.post("/", status_code=201)
def create_train(train: TrainCreate) -> TrainCreateResponse:
    stops: list[TrainStopsBase] = train.stops

    with Session(engine) as session:

        train_db = Train(**train.model_dump(exclude={"stops"}))
        session.add(train_db)

        with session.begin_nested():
            session.commit()

        for stop in stops:
            stop_db = Stops(**stop.model_dump(exclude_unset=True))
            stop_db.train_id = train_db.train_id
            
            session.add(stop_db)
        session.commit()
        
        train_response: TrainCreateResponse = TrainCreateResponse.model_validate(train_db, from_attributes=True)
        
    train_response.service_start = stops[0].departure_time
    train_response.service_end = stops[-1].arrival_time
    train_response.num_stations = len(stops)
    
    return train_response


@router.get("/")
def get_trains() -> list[TrainCreate]:
    with Session(engine) as session:
        trains = session.query(Train).all()
        trains_reponse: list[TrainCreate] = [TrainCreate.model_validate(train, from_attributes=True) for train in trains]

        for train in trains_reponse:
            train.stops = [TrainStopsBase.model_validate(stop, from_attributes=True) for stop in session.query(Stops).filter(Stops.train_id == train.train_id).all()]

        return trains_reponse

