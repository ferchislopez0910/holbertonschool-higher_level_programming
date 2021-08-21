#!/usr/bin/python3
"""Write a Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)"""


import urllib.request as request
import urllib.parse as par
import sys


if __name__ == '__main__':
    url = sys.argv[1]

    value = {'email': sys.argv[2]}
    data = par.urlencode(value)
    data = data.encode('ascii')

    req = request.Request(url, data)

    with request.urlopen(req) as response:
        r = response.read()
        print(r.decode('utf-8'))
