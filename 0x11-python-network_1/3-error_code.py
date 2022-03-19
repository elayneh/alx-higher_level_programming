#!/usr/bin/python3
""" send a request, display the response and handle the error"""
import urllib.request
import urllib.error
import sys

request = urllib.request.Request(sys.argv[1])
try:
    with urllib.request.urlopen(request) as response:
        response = response.decode("ascii")
        print(response.read())
except urllib.error.HTTPError as e:
    print("Error code: {}".format(e.code))
