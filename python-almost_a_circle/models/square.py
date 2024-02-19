#!/usr/bin/python3


"""
Write the class Square that inherits from Rectangle:

In the file models/rectangle.py
Class Square inherits from Base
Private instance attributes, each with its own public getter and setter:
__width -> width
__height -> height
__x -> x
__y -> y
Class constructor: def __init__(self, width, height, x=0, y=0, id=None):
Call the super class with id - this super call with use the logic of the
__init__ of the Base class
Assign each argument width, height, x and y to the right attribute
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor for Square class"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """String representation of Square"""
        return "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Getter for size attribute"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size attribute"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update method for Square"""
        if args:
            attributes = ["id", "size", "x", "y"]
            for i, value in enumerate(args):
                setattr(self, attributes[i], value)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Dictionary representation of Square"""
        return {'id': self.id, 'size': self.width, 'x': self.x, 'y': self.y}
