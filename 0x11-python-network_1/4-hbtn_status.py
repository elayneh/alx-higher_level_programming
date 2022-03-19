#!/usr/bin/python3
"""fetch https://alx-interanet.hbtn.io/status
    """
import requests

url = "https://intranet.hbtn.io/status"
out_put = requests.get(url)
print("Body response:")
print("\t- type: {}".format(type(out_put.text)))
print("\t- content: {}".format(out_put.text))
