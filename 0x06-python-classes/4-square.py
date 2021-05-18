#!/usr/bin/python3
"""def class Square that defines a square"""


class Square:
    """empty class Square that

    defines a square"""
    def __init__(self, size=0):
        """Created a module"""
        if isinstance(size, int):
            self.__size = size
            if size < 0:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """Def del area"""
        return self.__size ** 2

    @property
    def size(self):
        """Def del size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Def del value"""
        if isinstance(value, int):
            self.__size = value
            if value < 0:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
