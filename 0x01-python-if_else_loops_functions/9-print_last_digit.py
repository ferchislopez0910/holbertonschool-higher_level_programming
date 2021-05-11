#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        n = ((-1 * number) % 10)
        print(n, end='')
    else:
        n = number % 10
        print(n, end='')
    return (n)
