#!/usr/bin/python3
"""take URL, sent request and display the value to the given
    variable importing requests and sys only
    """
import requests
import sys

url = sys.argv[1]
response = requests.get(url)
print(response.headers.get("X-request-Id"))
