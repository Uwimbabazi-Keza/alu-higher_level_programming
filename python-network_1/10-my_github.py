#!/usr/bin/python3
"""Takes your GitHub credentials (username and password)
and uses the GitHub API to display your id"""

import requests
import sys
import requests.auth

if __name__ == '__main__':
    url = "https://api.github.com/user"
    username = sys.argv[1]
    password = sys.argv[2]
    info = (username, password)
    r = requests.get(url, auth=info)
    try:
        print(r.json()['id'])
    except Exception:
        print('None')
