#!/usr/bin/python3
"""
This module contains the class definition of a State and an instance Base
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create Base instance
Base = declarative_base()


class State(Base):
    """
    State class that links to the MySQL table states
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
