#!/usr/bin/python3
"""fetch https://alx-interanet.hbtn.io/status
    """
import requests


def fetch():
    url = "https://intranet.hbtn.io/status"
    out_put = requests.get(url)
    print("Body response:")
    print("\t- type: {}".format(type(out_put.text)))
    print("\t- content: {}".format(out_put.text))
if __name__ == "__main__":
    fetch()
