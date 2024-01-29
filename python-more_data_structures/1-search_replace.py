#!/usr/bin/python3
def search_replace(my_list, search, replace):
    idx = search - 1
    copied_list = my_list.copy()
    temp_list = copied_list.insert(idx, replace)
    return copied_list
