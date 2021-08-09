#!/usr/bin/python3
"""

Write a python file that contains the class
definition of a Stateand an instance
Base = declarative_base():
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()
"""Its a class of lib Alchemist """


class State(Base):
    """Class that to created table of bd"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    """ backref hace que se borre todo lo que
    modifique en city """
    cities = relationship("City", backref="state")
