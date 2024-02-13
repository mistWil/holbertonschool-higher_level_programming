#!/usr/bin/python3


"""
Write a class Square that inherits from Rectangle (9-rectangle.py).
(task based on 10-square.py).
Instantiation with size: def __init__(self, size)::
size must be private. No getter or setter
size must be a positive integer, validated by integer_validator
the area() method must be implemented
print() should print, and str() should return, the square description:
[Square] <width>/<height>
"""


"""
Import the BaseGeometry class
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""
Import the Rectangle class
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class inheriting from Rectangle
    """

    def __init__(self, size):
        """
        Initializes a Square instance
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """
        Returns a string representation of the square
        """
        return f"[Square] {self.__size}/{self.__size}"
