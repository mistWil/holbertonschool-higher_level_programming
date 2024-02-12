#!/usr/bin/python3


"""
Write a function that returns the list of available attributes
and methods of an object:

Prototype: def lookup(obj):
Returns a list object
You are not allowed to import any module
"""


def lookup(obj):
    return dir(obj)
