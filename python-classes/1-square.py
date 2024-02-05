#!/usr/bin/python3


"""
Write a class Square that defines a square by: (based on 0-square.py)

Private instance attribute: size
Instantiation with size (no type/value verification)
You are not allowed to import any module
"""


class Square:
    """
    class Square that defines a square
    """
    def __init__(self, size=0):
        self.__size = size
