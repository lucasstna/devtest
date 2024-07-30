from fastapi import FastAPI

class Elevator(FastAPI):
    def __init__(self, id, first_floor, penthouse_floor):
        super().__init__()

        self.current_floor = 0
        self.status = 'idle'
        self.id = id
        self.first_floor = first_floor
        self.penthouse_floor = penthouse_floor


    def update_current_elevator_status(self, status):
        self.status = status
