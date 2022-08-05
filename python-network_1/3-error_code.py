#!/usr/bin/python3
"""Script that takes in a URL, sends a request
to the URL & displays the body of the response"""

import urllib.error
import urllib.request
import sys

if __name__ == "__main__":
    """"task 3"""
    req = request.Request(argv[1])
    try:
        with request.urlopen(req) as r:
            print(r.read().decode('utf-8'))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
