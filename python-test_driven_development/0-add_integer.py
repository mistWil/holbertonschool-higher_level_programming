#!/usr/bin/python3


"""
    add function
    args : a & b must be int or float
    return a + b
"""


def add_integer(a, b=98):
    """
    Add two integers.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or float")
    return int(a) + int(b)
