#!/usr/bin/python3
"""
This module contains the class definition of a City
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """
    City class that links to the MySQL table cities

    Attributes:
        id: Auto-generated, unique integer, primary key, not null
        name: String with maximum 128 characters, not null  
        state_id: Integer, not null, foreign key to states.id
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
