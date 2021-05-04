#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    ln = len(sys.argv)
    argument = (sys.argv)
    if argument == 1:
        print('0')
    else:   
        sum = 0
        for i in (1, ln):
            sum += (int(sys.argv[i]))
        print('{}'.format(sum))
