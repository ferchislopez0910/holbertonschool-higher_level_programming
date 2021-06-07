#!/usr/bin/python3
from models.base import Base
"""2. First Rectangle """


class Rectangle(Base):
    """ class Rectangle that inherits from Base"""
    
    def __init__(self, width, height, x=0, y=0, id=None):
        """ First Rectangle """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)
    