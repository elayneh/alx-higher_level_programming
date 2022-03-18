#!/usr/bin/python3
"""Fetches header"""
import urllib.request, sys


def fetcher():
    """fetch the given code"""
    with urllib.request.urlopen(sys.argv[1]) as response:
        header = response.info()
        print(header["X-Request-Id"])

if __name__ == "__main__":
    fetcher()
