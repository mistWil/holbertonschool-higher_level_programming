#!/usr/bin/python


"""
Write a class Rectangle that inherits from BaseGeometry (7-base_geometry.py).
(task based on 8-rectangle.py)
Instantiation with width and height:
def __init__(self, width, height)::
width and height must be private. No getter or setter
width and height must be positive integers validated by integer_validator
the area() method must be implemented
print() should print, and str() should return, the following
rectangle description: [Rectangle] <width>/<height>
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
