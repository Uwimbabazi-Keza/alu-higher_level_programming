#!/usr/bin/python3
"""Python script fetches https://intranet.hbtn.io/status"""
import urllib.request
with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
    x = response.read()

print('Body response:\n\t- type: {}'.format(type(x)))
print('\t- x: {}'.format(x))
print('\t- utf8 x: {}'.format(x.decode('utf-8')))
