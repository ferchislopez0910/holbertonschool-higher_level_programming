#!/usr/bin/python3
""" Square that inherits from Rectangle """
from models.rectangle import Rectangle


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
        self.height = value

    def __str__(self):
        """ method so that it returns [Rectangle] """
        return str("[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width))

    def update(self, *args, **kwargs):
        """Update the class Square"""
        val = ['id', 'size', 'x', 'y']
        valarg = ['id', 'width', 'height', 'x', 'y']
        if args:
            for i in range(len(args)):
                setattr(self, valarg[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
    
    def to_dictionary(self):
        """pdate the class Rectangle by adding the public method"""
        return self.__dict__

