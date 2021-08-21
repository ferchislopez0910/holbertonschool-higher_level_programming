#!/usr/bin/python3
"""
Write a Python script that takes in a URL,
sends a request to the URL and displays the
 body of the response.
"""


import requests
import sys


if __name__ == '__main__':
    req = requests.get(sys.argv[1])
    status_code = req.status_code
    if status_code >= 400:
        print('Error code:', status_code)
    else:
        print(req.text)
