#!/usr/bin/python3


"""
* Write a class Student that defines a student by:
* Public instance attributes:
first_name
last_name
age
* Instantiation with first_name, last_name and age:
def __init__(self, first_name, last_name, age):
* Public method def to_json(self): that retrieves a dictionary
representation of a Student instance (same as 8-class_to_json.py)
* You are not allowed to import any module
"""


class Student:
    """Class named Student"""

    def __init__(self, first_name, last_name, age):
        """
        Using the init method to initialize public instance attributes

        Args:
        first_name
        last_name
        age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Public method that retries a dictionary representation"""
        return self.__dict__
