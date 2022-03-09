#!/usr/bin/python3
"""
contains the class city
"""

import sqlalchemy
from sqlalchemy import Column, Integer, String, Foreignkey
from model_state import Base, State


class City(Base):
    """Representation of a city"""
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, Foreignkey('state_id'))
