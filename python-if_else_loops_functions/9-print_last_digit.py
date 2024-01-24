#!/usr/bin/python3

def print_last_digit(number):

    if number < 0:
        last_digit = number % -10
        last_digit = last_digit * -1

    else:
        last_digit = number % 10

    print(last_digit, end="")
    return last_digit
