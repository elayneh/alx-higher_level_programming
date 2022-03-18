#!/usr/bin/python3
"""Send POST and display the response"""
import email
import urllib.request
import urllib.parse
import sys


def poster():
    url = sys.argv[1]
    email = {"email": sys.argv[2]}
    request = urllib.request.Request(url, urllib.parse.urlencode(email))
    with urllib.request.urlopen(request) as response:
        page = response.read()
        print(page.decode("utf-8"))

if __name__ == "__main__":
    poster()
