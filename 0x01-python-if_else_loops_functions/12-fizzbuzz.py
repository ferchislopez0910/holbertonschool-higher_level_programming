#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 100):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz ", end=" ")
        elif i % 3 == 0:
            i = "Fizz"
            print(i, end=" ")
        elif i % 5 == 0:
            i = "Buzz"
            print(i, end='')
        else:
            print(" ", i, end=" ")
