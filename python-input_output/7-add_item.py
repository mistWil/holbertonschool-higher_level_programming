#!/usr/bin/python3


"""
* Write a script that adds all arguments to a Python list,
and then save them to a file:
* You must use your function save_to_json_file from 5-save_to_json_file.py
* You must use your function load_from_json_file from 6-load_from_json_file.py
* The list must be saved as a JSON representation in a file named add_item.json
* If the file doesnt exist, it should be created
* You dont need to manage file permissions / exceptions.
"""

import json
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

args = sys.argv[1:]
filename = 'add_item.json'
with open(filename, 'a', encoding="utf-8") as file:
    try:
        my_list = load_from_json_file(filename)
    except Exception:
        my_list = []
    my_list.extend(args)
    save_to_json_file(my_list, filename)
