#!/usr/bin/python3
"""
Write a Python script that takes in a URL,
sends a request to the URL and displays the body
of the response (decoded in utf-8).
"""

import urllib.request as request
import urllib
import sys


if __name__ == '__main__':
    url = sys.argv[1]

    rqst = request.Request(url)
    try:
        with request.urlopen(rqst) as response:
            rta = response.read()
            print(rta.decode('utf-8'))
    except urllib.error.HTTPError as err:
        print('Error code:', err.code)
