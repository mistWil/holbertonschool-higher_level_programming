#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    copie_list = my_list.copy()
    if idx < 0 or idx >= len(my_list):
        return copie_list
    copie_list[idx] = element
    return copie_list
