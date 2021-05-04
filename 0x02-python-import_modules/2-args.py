#!/usr/bin/python3
import sys
if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("0 arguments.")
    elif len(sys.argv) == 2:
        print("1 argument:")
        print('1: {}'.format(sys.argv[1]))
    else:
        ln = len(sys.argv)
        print('{} arguments:'.format(ln - 1))
        for i in range(1, ln):
            print("{:} : {:}".format(i, sys.argv[i]))
