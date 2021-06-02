#!/usr/bin/python3
"""Write a function that reads a text file"""


def read_file(filename=""):
    """Write a function that reads a text file"""

    with open(filename, encoding='utf-8') as f:
        content = f.read()
        print(content, end='')
