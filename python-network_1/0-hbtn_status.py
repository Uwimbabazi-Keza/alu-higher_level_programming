#!/usr/bin/python3
"""Python script fetches https://intranet.hbtn.io/status"""
import urllib.request
with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
    content = response.read()

print('Body response:\n\t- type: {}'.format(type(content)))
print('\t- content: {}'.format(content))
print('\t- utf8 content: {}'.format(content.decode('utf-8')))
