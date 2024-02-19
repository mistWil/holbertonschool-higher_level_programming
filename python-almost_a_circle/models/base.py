#!/usr/bin/python3


"""
Write the first class Base:

Create a folder named models with an empty file __init__.py inside
with this file, the folder will become a Python package

Create a file named models/base.py:

Class Base:
private class attribute __nb_objects = 0
class constructor: def __init__(self, id=None)::
if id is not None, assign the public instance attribute id
with this argument value - you can assume id is an integer
and you don’t need to test the type of it
otherwise, increment __nb_objects and assign the new value
to the public instance attribute id
"""


import json


class Base:
    """Class named Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Def id"""
        self.id = id

        if self.id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
