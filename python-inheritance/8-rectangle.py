#!/usr/bin/python3


"""
* Write a class BaseGeometry
* Public instance method: that raises an Exception
* Public instance method that validates value
* You are not allowed to import any module
"""


class BaseGeometry:
    """class 'BaseGeometry'"""

    def area(self):
        """Public instance method that raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Public instance method that validates value"""
        if not type(value) is int:
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """New class Rectangle that inherits from parent class"""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
