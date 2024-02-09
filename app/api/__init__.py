from fastapi import APIRouter, Query
from fastapi.responses import JSONResponse

from .modules import include_api_routers

from sqlalchemy.orm import Session
from app.db_utils import engine

from app.api.modules.station.models import Station
from app.api.modules.train.models import Train, Stops

router = APIRouter(prefix="/api")
include_api_routers(router)

def dfs(from_station: Station, to_staion: Station, visited: set[int], path: list[int], session: Session):
    path = path[:]

    visited.add(from_station.station_id)

    if from_station == to_staion:
        return path
    
    for stop in session.query(Stops).filter(Stops.station_id == from_station.station_id).all():
        next_stop: Stops = session.query(Stops).get(stop.stop_id + 1)
        if next_stop:
            next_station: Station = session.query(Station).get(next_stop.station_id)
            
            if next_station.station_id not in visited:
                path.append(next_station)
                dfs(next_station, to_staion, visited, path, session)
    return path


@router.get("/")
def routes(from_station_id: str = Query(alias="from"), to: int = None, optimize: str = "cost"):
    with Session(engine) as session:
        from_station: Station = session.query(Station).get(from_station_id)
        to_staion: Station = session.query(Station).get(to)

        if not from_station or not to_staion:
            return JSONResponse({"message": f"no routes available from station: {from_station_id} to station: {to}"}, status_code=404)
        

        path = dfs(from_station, to_staion, set(), [from_station], session)
        if path[-1] and path[-1].station_id != to_staion.station_id:
            return JSONResponse({"message": f"no routes available from station: {from_station_id} to station: {to}"}, status_code=404)
    
    return path
     
