#!/usr/bin/python3
for int in range(0, 100):
    if int == 99:
        print("{:02d}".format(int))
    else:
        print("{:02d}, ".format(int), end="")
