#!/usr/bin/python


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
    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.y = y
        super().__init__(id)

        @property
        def width(self):
            """Getter"""
            return self.__width

        @width.setter
        def width(self, value):
            """Setter"""
            self.__width = value

        @property
        def height(self):
            """Getter"""
            return self.__height

        @height.setter
        def height(self, value):
            """Setter"""
            self.__height = value

        @property
        def x(self):
            """Getter"""
            return self.__x

        @x.setter
        def x(self, value):
            """Setter"""
            self.__x = value

        @property
        def y(self):
            """Getter"""
            return self.__width

        @y.setter
        def y(self, value):
            """Setter"""
            self.__y = value