#!/usr/bin/python3

import urllib.request

def fun_fetch():
    with urllib.request.urlopen("https://intranet.hbtn.io/status") as response:
        page = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(page)))
        print("\t- content: {}".format(page))
        print("\t- utf8 content: {}".format(page.decode("utf-8")))

if __name__ == "__main__":
    fun_fetch()
