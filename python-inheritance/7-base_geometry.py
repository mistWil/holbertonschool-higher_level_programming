#!/usr/bin/python3

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
