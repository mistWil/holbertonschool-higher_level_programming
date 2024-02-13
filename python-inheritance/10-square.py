#!/usr/bin/python3


"""
Write a class Square that inherits from Rectangle (9-rectangle.py):
Instantiation with size: def __init__(self, size)::
size must be private. No getter or setter
size must be a positive integer, validated by integer_validator
the area() method must be implemented
"""


class BaseGeometry:
    """
    class 'BaseGeometry'
    """

    def area(self):
        """
        Public instance method that raises an exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Public instance method that validates value
        """
        if not type(value) is int:
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """
    New class Rectangle that inherits from parent class
    """

    def __init__(self, width, height):
        super().__init__()
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Method to calculate the area of the rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Method to return the string representation of the rectangle
        """
        return f"[Rectangle] {self.__width}/{self.__height}"


class Square(Rectangle):
    """
    New class Square that inherits from Rectangle
    """

    def __init__(self, size):
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Method to calculate the area of the rectangle
        """
        return self.__size * self.__size

    def __str__(self):
        """
        Method to return the string representation of the square
        """
        return f"[Rectangle] {self.__size}/{self.__size}"
