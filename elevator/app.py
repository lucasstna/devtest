from fastapi import FastAPI

from routers import elevator_routes


app = FastAPI(
    id = 1,
    first_garage_floor = 0,
    penthouse_floor = 10
)

app.include_router(elevator_routes.router)
