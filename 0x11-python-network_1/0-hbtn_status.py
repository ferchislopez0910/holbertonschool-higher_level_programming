#!/usr/bin/python3
"""Write a Python script that fetches https://intranet.hbtn.io/status"""
import urllib.request


with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
    url = response.read()
    print('Body response:')
    print('\t- type:', type(url))
    print('\t- content:', url)
    print('\t- utf8 content:', url.decode('UTF-8'))
