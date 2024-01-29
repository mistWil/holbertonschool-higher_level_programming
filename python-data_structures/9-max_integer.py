#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        higher = my_list[0]
        for i in range(1, len(my_list)):
            if my_list[i] > higher:
                higher = my_list[i]
        return higher
    else:
        return None
