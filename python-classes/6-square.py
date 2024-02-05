#!/usr/bin/python3
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
