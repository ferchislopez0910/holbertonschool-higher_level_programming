#!/usr/bin/python3
for i in range(0, 10):
    for j in range(0, 10):
        if i < j and (i * 10) + j < 89:
            print('{:d}{:d}'.format(i, j), end=", ")
        if i == 8 and j == 9:
            print('{:d}{:d}'.format(i, j))
