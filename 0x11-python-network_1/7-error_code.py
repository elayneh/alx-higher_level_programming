#!/usr/bin/python3
"""display the staus code and other discription based on the given condition
"""
import sys
import requests

if __name__=="__main__":
    
    url = sys.argv[1]
    response = requests.get(url)
    if(response.status_code >= 400):
        print("Error code: {}".format(response.status_code))
    else:
        print(response)
