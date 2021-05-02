#!/usr/bin/python3
for i in range(0, 100):
    if i < 99:
        print(i, end=", ")
    elif i == 99:
        print('{:d} '.format(i))
