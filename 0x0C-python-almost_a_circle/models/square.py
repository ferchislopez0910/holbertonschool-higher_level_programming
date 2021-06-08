#!/usr/bin/python3
from models.rectangle import Rectangle
""" Square that inherits from Rectangle """


class Square(Rectangle):
    """Class Square"""
    def __init__(self, size, x=0, y=0, id=None):
        """ def size, x=0, y=0, id=None"""
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        return self.width
    
    @size.setter
    def size(self, value):
        self.width = value

    def __str__(self):
        """ method so that it returns [Rectangle] """
        return str("[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width))