#!/usr/bin/python3
"""
Write a class Rectangle that defines a rectangle:
* Private instance attribute: width
* Private instance attribute: height
* Instantiation with optional width and heigh
* Public instance method: def area(self): that returns the rectangle area
* Public instance method: def perimeter(self): that returns
the rectangle perimeter
* You are not allowed to import any module
"""


class Rectangle:
    """
    Class named Rectangle
    """
    def __init__(self, width=0, height=0):
        """
        Use of the init method to create two private instance attributes

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Property decorator to turn the width method into a getter
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter decorator allowing to modify the value of width method
        """
        if not isinstance(value, int):
            """
            Raising a TypeError exception as the width/value must be an integer
            """
            raise TypeError("width must be an integer")
        elif value < 0:
            """
            Raising a ValueError exception as the size/value must be >= 0
            """
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        Property decorator to turn the width method into a getter
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter decorator allowing to modify the value of width method
        """
        if not isinstance(value, int):
            """
            Raising a TypeError exception as the width/value must be an integer
            """
            raise TypeError("height must be an integer")
        elif value < 0:
            """
            Raising a ValueError exception as the size/value must be >= 0
            """
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        Public instance method that returns the rectangle area

        Returns:
            int: the area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Public instance method that returns the rectangle perimeter

        Returns:
            int: the perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            print("")
        else:
            return "\n".join("#" * self.__width for x in range(self.__height))
