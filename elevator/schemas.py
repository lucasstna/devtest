from datetime import datetime

from pydantic import BaseModel


class ElevatorDemand(BaseModel):
    id: int
    elevator_id: int
    status: str
    current_floor: int
    target_floor: int



class Message(BaseModel):
    message: str