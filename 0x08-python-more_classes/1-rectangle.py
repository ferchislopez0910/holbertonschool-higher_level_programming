#!/usr/bin/python3
"""empty class Square that defines a square"""


class Rectangle:
    """empty class Square that

    defines a square"""
    def __init__(self, width=0, height=0):
        #Created the module
        if isinstance(height, int):
            self.__height = height
            if height < 0:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
        
        if isinstance(width, int):
            self.__width = width
            if width < 0:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
  
    @property
    def width(self):
        """Def del width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Def del height"""
        if isinstance(value, int):
            self.__width = value
            if value < 0:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
    
    @property
    def height(self):
        """Def del height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Def del height"""
        if isinstance(value, int):
            self.__height = value
            if value < 0:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
