#!/usr/bin/python3
""" take the url and send request to the url finally display the value of the X-Request-Id """
import urllib.request, sys

def header():
    with urllib.request.urlopen(sys.argv[1]) as resp:
        header = resp.info()
        print(header["X-Request-Id"])

if __name__ == "__main__":
    header()
