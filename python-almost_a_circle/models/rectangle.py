#!/usr/bin/python3


"""
Write the class Rectangle that inherits from Base:

In the file models/rectangle.py
Class Rectangle inherits from Base
Private instance attributes, each with its own public getter and setter:
__width -> width
__height -> height
__x -> x
__y -> y
Class constructor: def __init__(self, width, height, x=0, y=0, id=None):
Call the super class with id - this super call with use the logic of the
__init__ of the Base class
Assign each argument width, height, x and y to the right attribute
"""


from models.base import Base


class Rectangle(Base):
    """Base class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor to initialize the Rectanble instance

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
            x (int): coordinate of the rectangle
            y (int): coordinate of the rectangle
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter"""
        if value is not isinstance(value, int):
            raise TypeError('{} must be an integer'.format(value))
        if value <= 0:
            raise ValueError('{} must be > 0'.format(value))
        self.__width = value

    @property
    def height(self):
        """Getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter"""
        if value is not isinstance(value, int):
            raise TypeError('{} must be an integer'.format(value))
        if value <= 0:
            raise ValueError('{} must be > 0'.format(value))
        self.__height = value

    @property
    def x(self):
        """Getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter"""
        if value is not isinstance(value, int):
            raise TypeError('{} must be an integer'.format(value))
        if value < 0:
            raise ValueError('{} must be >= 0'.format(value))
        self.__x = value

    @property
    def y(self):
        """Getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter"""
        if value is not isinstance(value, int):
            raise TypeError('{} must be an integer'.format(value))
        if value < 0:
            raise ValueError('{} must be >= 0'.format(value))
        self.__y = value
