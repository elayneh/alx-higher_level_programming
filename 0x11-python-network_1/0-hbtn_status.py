#!/usr/bin/python3

import urllib.request

def fun_fetch():
    request = urllib.request.Request("https://intranet.hbtn.io/status")
    with urllib.request.urlopen(request) as response:
        page = response.read()
        status = page.decode("utf-8")
        print("Body response:")
        print("\t- type: {}".format(type(page)))
        print("\t- content: {}".format(page))
        print("\t- utf8 content: {}".format(status))
if __name__ == "__main__":
    fun_fetch()
