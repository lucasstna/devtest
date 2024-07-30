from database import models, schemas

from sqlalchemy.orm import Session


def create_demand_registry(session: Session, demand: schemas.ElevatorDemand):

    demand_db = models.ElevatorDemand(
        id = demand.id,
        elevator_id = demand.elevator_id,
        initial_floor = demand.initial_floor,
        target_floor = demand.target_floor
    )

    session.add(demand_db)
    session.commit()
    session.refresh(demand_db)

    return demand_db


def get_elevator_demand_by_id(session: Session, demand_id: int):

    return session.query(models.ElevatorDemand).filter(models.ElevatorDemand.id == demand_id).first()


def delete_demand(session: Session, demand: schemas.ElevatorDemand):

    session.delete(demand)
    session.commit()

    return demand

def get_demands(session: Session):

    return session.query(models.ElevatorDemand).all()