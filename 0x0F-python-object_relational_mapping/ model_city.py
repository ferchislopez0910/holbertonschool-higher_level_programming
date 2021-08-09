#!/usr/bin/python3
"""

Write a python file that contains the class
definition of a Stateand an instance
Base = declarative_base():
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
"""Its a class of lib Alchemist """


class City(Base):
    """Class that to created table of bd"""
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))
