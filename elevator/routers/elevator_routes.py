from fastapi import HTTPException

from elevator import ElevatorRouter

from http import HTTPStatus

from schemas import ElevatorDemand, Message


router = ElevatorRouter(
    prefix = "/elevator"
)

@router.get("/", status_code = HTTPStatus.OK, response_model = Message)
def get_root():
    return {"message" : "Elevator service. Please use /docs to see the API documentation."}


@router.post('/{floor_id}', status_code = HTTPStatus.CREATED, response_model = ElevatorDemand)
def call_elevator(floor_id: int, elevator_id: int):
    if floor_id < app.first_garage_floor and floor_id > app.penthouse_floor:
        raise HTTPException(
            status_code = HTTPStatus.BAD_REQUEST, detail = "Invalid floor number."
        )
    
    elevator_demand =  ElevatorDemand(
        id = len(app.database) + 1,
        elevator_id = elevator_id, 
        status = "moving",
        current_floor = app.current_floor,
        target_floor = floor_id
    )

    app.database.append(elevator_demand)

    sleep(20)

    return elevator_demand


@router.get('/status', status_code = HTTPStatus.OK, response_model = Message)
def get_elevator_status():

    return {'status' : app.database[-1].status}


@router.put('/status/{status}', response_model = ElevatorDemand)
def update_elevator_status(status: str):
    # need to check if status is valid, getting it from database

    app.database[-1].status = status

    return app.database[-1]


@router.delete('/{demand_id}', response_model = Message)
def delete_elevator_demand(demand_id: int):
    del app.database[demand_id - 1]

    return {"message" : "Elevator demand has been deleted."}
# @router.get('/{floor_id}', response_model=ElevatorDemand)
# def get_elevator_demand(floor_id: int):
    
#     if ()

#     return {"message": "No elevator demand for this floor."}