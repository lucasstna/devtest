from fastapi import APIRouter

class ElevatorRouter(APIRouter):
    def __init__(self, id, first_garage_floor, penthouse_floor):
        super().__init__()

        self.current_floor = 0
        self.database = []
        self.id = id
        self.first_garage_floor = first_garage_floor
        self.penthouse_floor = penthouse_floor
