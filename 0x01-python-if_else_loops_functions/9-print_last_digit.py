#!/usr/bin/python3
def print_last_digit(number):
    if number >= 10:
        return (number % 10)
    elif number < 0:
        n = number * -1
        return ((n) % 10)
    return(number)
