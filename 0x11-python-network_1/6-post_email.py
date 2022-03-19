#!/usr/bin/python3
"""take url and email address, send a post request
finally display the response
"""
import requests
import sys

value = {"email": sys.argv[2]
         }
response = requests.post(sys.argv[1], data=value)
print(response)
