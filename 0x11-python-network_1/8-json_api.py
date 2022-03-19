#!/usr/bin/python3
"""take a letter and post a request to http://0.0.0.0:5000/search_user
"""

import requests
import sys

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    letter = "" if len(sys.argv) == 1 else sys.sys.argv[1]
    Value = {'q': ""}

    response = requests.post(url, data=Value)
    try:
        resp = response.json()
        if resp == {}:
            print("No result")
        else:
            print("[{}] {}".format(resp.get("id"), resp.get("name")))
    except ValueError:
        print("Not a valid JSON")
