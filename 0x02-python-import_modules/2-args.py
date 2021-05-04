#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argument = len(sys.argv) 
    if argument == 1:
        print("0 arguments.")
    elif argument == 2:
        print(argument, "argument:")
        print("1: {}".format(sys.argv[1]))
    else:
        print('{} arguments:'.format(len(sys.argv) - 1))
        ln = (len(sys.argv))
        for i in range(1, ln):
            print('{} : {}'.format(i, sys.argv[i]))
