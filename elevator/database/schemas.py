from pydantic import BaseModel


class ElevatorDemand(BaseModel):
    id: int
    elevator_id: int
    initial_floor: int
    target_floor: int

    class Config:
        orm_mode = True


class Elevator(BaseModel):
    id: int
    name: str
    demands: list[ElevatorDemand]


class Message(BaseModel):
    message: str


class Demands(BaseModel):
    demands: list[ElevatorDemand]