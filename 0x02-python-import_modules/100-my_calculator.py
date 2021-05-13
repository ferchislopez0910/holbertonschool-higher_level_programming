#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        quit(1)
    a = int(argv[1])
    b = int(argv[3])
    operator = ['+', '-', '*', '/']
    from calculator_1 import add, sub, mul, div
    operactions = [add, sub, mul, div]
    for i, j in enumerate(operator):
        if argv[2] == j:
            print("{} {} {} = {}".format(a, j, b, operactions[i](a, b)))
            break
    else:
        print("Unknown operator. Available operators: +, -, * and /")
