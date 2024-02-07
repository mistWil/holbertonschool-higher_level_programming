#!/usr/bin/python3


"""
_summary_

Write a class Rectangle that defines a rectangle by.

Private instance attribute: width:
property def width(self): to retrieve it
property setter def width(self, value): to set it:
width must be an integer, otherwise raise a TypeError
exception with the message width must be an integer
if width is less than 0, raise a ValueError exception
with the message width must be >= 0
Private instance attribute: height:
property def height(self): to retrieve it
property setter def height(self, value): to set it:
height must be an integer, otherwise raise a TypeError
exception with the message height must be an integer
if height is less than 0, raise a ValueError exception
with the message height must be >= 0
Instantiation with optional width and height:
def __init__(self, width=0, height=0):
Public instance method: def area(self): that
returns the rectangle area
Public instance method: def perimeter(self):
that returns the rectangle perimeter:
if width or height is equal to 0, perimeter
has to be equal to 0
print() and str() should print the rectangle
with the character #: (see example below)
if width or height is equal to 0, return an
empty string
repr() should return a string representation
of the rectangle to be able to recreate a new
instance by using eval()
"""


class Rectangle:
    """
    Rectangle class representing a rectangle.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle instance.

        Args:
            width (int): The width of the rectangle (default 0).
            height (int): The height of the rectangle (default 0).

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Represent the rectangle as a string of '#' characters.

        Returns:
            str: The string representation of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle = ""
        for i in range(self.__height):
            rectangle += "#" * self.__width
            if i != self.__height - 1:
                rectangle += "\n"
        return rectangle

    def __repr__(self):
        """
        Return a string representation of the rectangle.

        This representation can be used to recreate the rectangle using eval().

        Returns:
            str: A string representation of the rectangle.
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)
