#!/usr/bin/python3


"""
* Write a function that returns True if the object is an instance of,
or if the object is an instance of a class that inherited from,
the specified class ; otherwise False.
* Prototype: def is_kind_of_class(obj, a_class):
* You are not allowed to import any module
"""


def inherits_from(obj, a_class):
    """
    Function that returns True if the object is an instance
    from a class that inherited from the specified class
    """
    if type(obj) is a_class:
        return False
    return issubclass(type(obj), a_class)
