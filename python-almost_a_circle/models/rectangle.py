#!/usr/bin/python3


from models.base import Base


class Rectangle(Base):
    """Base class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor to initialize the Rectangle instance

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
            x (int): coordinate of the rectangle
            y (int): coordinate of the rectangle
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """Getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """Getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter"""
        if not isinstance(value, int):
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """Getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter"""
        if not isinstance(value, int):
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """Public method that returns the area of the rectangle"""
        return self.width * self.height

    def display(self):
        """Public method that prints the rectangle in stdout"""
        for i in range(self.y):
            print()
        for j in range(self.height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        return f'[Rectangle] ({self.id}) {self.x}/{self.y} - ' \
               f'{self.width}/{self.height}'

    def update(self, *args, **kwargs):
        """
        Public method that assigns a key/value argument to attributes
        Args:
            args: list of no keyword arguments
            kwargs: list of keyword arguments
        """
        if args and args is not None:
            attributes = ["id", "width", "height", "x", "y"]
            for attr, value in zip(attributes, args):
                setattr(self, attr, value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return dictionary representation of Rectangle"""
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }

    @classmethod
    def create(cls, **kwargs):
        """
        Create a new instance of Rectangle from a dictionary of parameters.
        """
        if 'id' in kwargs:
            new_id = kwargs['id']
            del kwargs['id']
        else:
            new_id = None
        width = kwargs.get('width', None)
        height = kwargs.get('height', None)
        x = kwargs.get('x', 0)
        y = kwargs.get('y', 0)
        return cls(width, height, x, y, id=new_id)
