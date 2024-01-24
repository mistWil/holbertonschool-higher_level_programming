#!/usr/bin/python3

def uppercase(str):

    result = ""

    for i in range(len(str)):

        if ord('a') <= ord(str[i]) <= ord('z'):
            result += chr(ord(str[i]) - 32)

        else:
            result += str[i]

    print(result)
