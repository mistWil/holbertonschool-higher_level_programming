#!/usr/bin/env python3
def fizzbuzz():
    for i in range(1, 101):
        if i == 3 or i % 3 == 0 and i % 5 != 0:
            print("{}".format("Fizz"), end=" ")
        elif i == 5 or i % 5 == 0 and i % 3 != 0:
            print("{}".format("Buzz"), end=" ")
        elif i % 3 == 0 and i % 5 == 0:
            print("{}".format("FizzBuzz"), end=" ")
        else:
            print("{}".format(i), end=" ")
