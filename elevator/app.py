
from database import models
from database.database import SessionLocal, engine
from database.schemas import ElevatorDemand, Message, Demands

from dependencies import get_session

from elevator import Elevator

from fastapi import Depends, HTTPException

from http import HTTPStatus

from sqlalchemy.orm import Session

from time import sleep

from utils import create_demand_registry, get_elevator_demand_by_id, delete_demand, get_demands


models.Base.metadata.create_all(bind = engine)

app = Elevator(
    id = 1,
    first_floor = -1,
    penthouse_floor = 10
)


@app.get("/", status_code = HTTPStatus.OK, response_model = Message)
def get_root():
    return {"message" : "Elevator service. Please use /docs to check API documentation."}


@app.post('/elevator/{floor_id}', status_code = HTTPStatus.CREATED, response_model = ElevatorDemand)
def call_elevator(floor_id: int, session: Session = Depends(get_session)):
    if floor_id < app.first_floor or floor_id > app.penthouse_floor:
        raise HTTPException(
            status_code = HTTPStatus.BAD_REQUEST, detail = "Invalid floor number."
        )

    elevator_demand = create_demand_registry(
        session,
        ElevatorDemand(
            id = session.query(models.ElevatorDemand).count() + 1,
            elevator_id = app.id,
            initial_floor = app.current_floor,
            target_floor = floor_id
        )
    )

    sleep(2)

    app.current_floor = floor_id

    return elevator_demand
    

@app.delete('/elevator/{demand_id}', status_code = HTTPStatus.OK, response_model = Message)
def delete_elevator_demand(demand_id: int, session: Session = Depends(get_session)):
    demand = get_elevator_demand_by_id(session, demand_id)

    if not demand:
        raise HTTPException(
            status_code = HTTPStatus.NOT_FOUND, detail = "Elevator demand not found."
        )
    
    delete_demand(session, demand)
    return {"message" : "Elevator demand has been deleted."}


@app.get('/elevator/demands', status_code = HTTPStatus.OK, response_model = Demands)
def get_all_elevator_demands(session: Session = Depends(get_session)):
    return {'demands' : get_demands(session)}


@app.get('/elevator/{demand_id}', status_code = HTTPStatus.OK, response_model = ElevatorDemand)
def get_elevator_demand(demand_id: int, session: Session = Depends(get_session)):
    demand = get_elevator_demand_by_id(session, demand_id)

    if not demand:
        raise HTTPException(
            status_code = HTTPStatus.NOT_FOUND, detail = "Elevator demand not found."
        )

    return demand
