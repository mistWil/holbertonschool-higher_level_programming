#!/usr/bin/python3


"""
Write a class BaseGeometry (based on 6-base_geometry.py).

Public instance method: def area(self): that raises an Exception
with the message area() is not implemented
Public instance method: def integer_validator(self, name, value):
that validates value:
you can assume name is always a string
if value is not an integer: raise a TypeError exception, with the message
<name> must be an integer
if value is less or equal to 0: raise a ValueError exception with the
message <name> must be greater than 0
"""


class BaseGeometry:
    """
    BaseGeometry class.
    """

    def area(self):
        """
        Computes the area.

        Raises:
            Exception: Always raises an Exception with
            the message "area() is not implemented".
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the value.

        Args:
            name (str): The name of the value.
            value (int): The value to validate.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
