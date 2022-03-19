#!/usr/bin/python3
"""take url and email address, send a post request
finally display the response
"""
import requests
import sys
if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]
             }
    response = requests.post(url, data=value)
    print(response)
