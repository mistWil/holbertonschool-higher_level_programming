#!/usr/bin/python3


"""
Write a function that creates an Object from a “JSON file”:
Prototype: def load_from_json_file(filename):
You must use the with statement
You don’t need to manage exceptions if the JSON string doesn’t
represent an object.
"""


import json


def load_from_json_file(filename):
    """Creates an Object from a “JSON file”"""
    with open(filename, mode="r", encoding="utf-8") as file:
        return json.load(file)
