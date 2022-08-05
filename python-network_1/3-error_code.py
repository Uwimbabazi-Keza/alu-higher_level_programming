#!/usr/bin/python3
"""Script that takes in a URL, sends a request
to the URL & displays the body of the response"""

import urllib.error
import urllib.request
import sys

if __name__ == "__main__":
    """"task 3"""
    url = sys.argv[1]
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as r:
            r = response.read()
            print(r.decode("ascii"))
    except urllib.error.HTTPError as error:
        print("Error code: {}".format(error.code))
