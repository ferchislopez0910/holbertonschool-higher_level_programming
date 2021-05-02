#!/usr/bin/python3
def uppercase(str):
    ln = len(str)

    for i in range(ln):
        if i >= 'a' and i <= 'z':
            i = chr(ord(i) - 32)
            print('{:}'.format(i), end="")
        print('{:}'.format(i), end="")
