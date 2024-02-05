#!/usr/bin/python3


"""
Write a class Square that defines a square by:
(based on 5-square.py)

Private instance attribute: size:
property def size(self): to retrieve it
property setter def size(self, value): to set it:
size must be an integer, otherwise raise a TypeError
exception with the message size must be an integer
if size is less than 0, raise a ValueError exception
with the message size must be >= 0
Private instance attribute: position:
property def position(self): to retrieve it
property setter def position(self, value): to set it:
position must be a tuple of 2 positive integers, otherwise
raise a TypeError exception with the message position must
be a tuple of 2 positive integers
Instantiation with optional size and optional position:
def __init__(self, size=0, position=(0, 0)):
Public instance method: def area(self):
that returns the current square area
Public instance method: def my_print(self):
that prints in stdout the square with the character #:
if size is equal to 0, print an empty line
position should be use by using space - Don’t fill
lines by spaces when position[1] > 0
You are not allowed to import any module
"""



class Square:
    """
    Defines a square with private attributes size and position.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a square with a specified size and position.

        Args:
            size (int): The size of the square's side.
            position (tuple): The position of the square as
            a tuple of two positive integers.

        Raises:
            TypeError: If size is not an integer or position
            is not a tuple of two positive integers.
            ValueError: If size is less than 0 or position
            contains non-positive integers.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Getter method to retrieve the size attribute.

        Returns:
            int: The size of the square's side.
        """
        return self.__size

    @size.setter
    def size(self, value):
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

    @property
    def position(self):
        """
        Getter method to retrieve the position attribute.

        Returns:
            tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter method to set the position attribute.

        Args:
            value (tuple): The new position value.

        Raises:
            TypeError: If value is not a tuple of two positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
           not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square using the '#' character.

        If size is equal to 0, prints an empty line.
        Uses the position attribute for spacing.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
