#!/usr/bin/python3

"""
Import the BaseGeometry class
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""
Import the Rectangle class
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """New subclass Square that inherits from subclass Rectangle"""

    def __init__(self, size):
        self.__size = size
        super().integer_validator("size", size)
        super().__init__(self.__size, self.__size)

    def area(self):
        """Public instance method inherited from parent class"""
        return self.__size * self.__size
