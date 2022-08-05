#!/usr/bin/python3
"""Takes your GitHub credentials (username and password)
and uses the GitHub API to display your id"""

import requests
import sys
import requests.auth
if __name__ == "__main__":
    username = HTTPBasicAuth(sys.argv[1])
    password = HTTPBasicAuth(sys.argv[2])
    req = requests.get('https://api.github.com/user',
                       auth=(username, password))
    print(req.json().get('id'))
