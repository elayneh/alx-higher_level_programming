#!/usr/bin/python3
"""fetch https://alx-interanet.hbtn.io/status
    """
import sys
import urllib.request


def fetch():
    url = "https://alx-intranet.hbtn.io/status"
    reqst = urllib.request.Request(url)
    with urllib.request.urlopen(reqst) as resp:
        out_put = resp.read()
        print("Body response:")
        print("\t- type: {}".format(type(out_put)))
        print("\t- content: {}".format(out_put))
if __name__ == "__main__":
    fetch()
