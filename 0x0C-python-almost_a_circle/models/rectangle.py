#!/usr/bin/python3
from models.base import Base
"""2. First Rectangle """


class Rectangle(Base):
    """ class Rectangle that inherits from Base"""
    __width = None
    __height = None
    __x = 0
    __y = 0

    def __init__(self, width, height, x=0, y=0, id=None):
        """ First Rectangle """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """width"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """height"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """x"""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value <= 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y"""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value <= 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """area rectangle"""
        return (self.__width * self.__height)

    def display(self):
        """that prints in stdout the Rectangle instance with the character #"""
        for l in range(self.y):
            print()

        for i in range(self.__height):
            for k in range(self.x):
                print(' ', end='')
            for j in range(self.__width):
                print("#", end="")
            print("")

    def __str__(self):
        """ method so that it returns [Rectangle] """
        return str("[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """That assigns an argument to each attribute: """
        if args:
            if len(args) == 1:
                self.id = args[0]
            else:
                self.id
            if len(args) == 2:
                self.width = args[1]
            else:
                self.width
            if len(args) == 3:
                self.height = args[2]
            else:
                self.height
            if len(args) == 4:
                self.x = args[3]
            else:
                self.x
            if len(args) == 5:
                self.y = args[4]
            else:
                self.y
        else:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                if key == 'width':
                    self.width = value
                if key == 'height':
                    self.height = value
                if key == 'x':
                    self.x = value
                if key == 'y':
                    self.y = value
                

