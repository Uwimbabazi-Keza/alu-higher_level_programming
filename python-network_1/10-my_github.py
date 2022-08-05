#!/usr/bin/python3
"""Takes your GitHub credentials (username and password)
and uses the GitHub API to display your id"""

import requests
import sys

url = 'https://api.github.com/user'

if __name__ == "__main__":
    res = requests.get(url, auth=(sys.argv[1], sys.argv[2])).json()
    if 'id' in res:
        print(res['id'])
    else:
        print(None)
