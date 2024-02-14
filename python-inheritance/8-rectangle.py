#!/usr/bin/python3


BaseGeometry = __import__('7-base_geometry').BaseGeometry


"""
* Write a class BaseGeometry
* Public instance method: that raises an Exception
* Public instance method that validates value
* You are not allowed to import any module
"""




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
