#!/usr/bin/python3
"""Takes your GitHub credentials (username and password)
and uses the GitHub API to display your id"""

import requests
import sys
import requests.auth

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    response = requests.get(
        url="https://api.github.com/user",
        auth=(requests.auth.HTTPBasicAuth(
            username,
            password
        )))
    try:
        json_response = response.json()
        print("{}".format(json_response["id"]))
    except:
        print(None))
