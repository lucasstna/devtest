from .database import Base

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class Elevator(Base):
    __tablename__ = "elevator"

    id = Column(Integer, primary_key = True, index = True)
    name = Column(String)
    
    demands = relationship("ElevatorDemand", back_populates = "elevator")


class ElevatorDemand(Base):
    __tablename__ = "elevator_demand"

    id = Column(Integer, primary_key = True, index = True)
    elevator_id = Column(Integer, ForeignKey("elevator.id"), unique = False)
    status_id = Column(Integer)
    initial_floor = Column(Integer)
    target_floor = Column(Integer)
    
    elevator = relationship("Elevator", back_populates = "demands")
    