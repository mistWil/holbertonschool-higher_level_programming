#!/usr/bin/python3


"""
    Write a class Square that defines a square by: (based on 3-square.py)

Private instance attribute: size:
property def size(self): to retrieve it
property setter def size(self, value): to set it:
size must be an integer, otherwise raise a TypeError
exception with the message size must be an integer
if size is less than 0, raise a ValueError exception
with the message size must be >= 0
Instantiation with optional size: def __init__(self, size=0):
Public instance method: def area(self): that returns the
current square area
You are not allowed to import any module
"""


class Square:
    """
    Defines a square with a private attribute size.
    """

    def __init__(self, size=0):
        """
        Initializes a square with a side of the specified size.

        Args:
            size (int): The size of the square's side.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.size = size

    def fget_size(self):
        """
        Getter method to retrieve the size attribute.

        Returns:
            int: The size of the square's side.
        """
        return self.__size

    def fset_size(self, value):
        """
        Setter method to set the size attribute.

        Args:
            value (int): The new size value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    # Use property() to create the property with fget and fset methods
    size = property(fget=fget_size, fset=fset_size)

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
