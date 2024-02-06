#!/usr/bin/python3


"""
    Prints the name in the format "My name is <first name> <last name>"

    :param first_name: The first name (string)
    :param last_name: The last name (string, default is "")
    :raises TypeError: If first_name or last_name is not a string
"""


def say_my_name(first_name, last_name=""):
    """
    Prints the name
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    if last_name:
        print("My name is {} {}".format(first_name, last_name))
    else:
        print("My name is {}".format(first_name))
