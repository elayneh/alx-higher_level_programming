#!/usr/bin/python3
""" take the url and send request to the url finally display the value of the X-Request-Id """
import urllib.request, sys

def fetcher():
    """function to fetch"""
    with urllib.request.urlopen(sys.argv[1]) as response:
        header = response.info()
        print(header["X-Request-Id"])

if __name__ == "__main__":
    fetcher()
