#!/usr/bin/env python3
"""
Script that fetches https://alu-intranet.hbtn.io/status
and displays the body response information.
"""
import requests

if __name__ == "__main__":
    url = "https://alu-intranet.hbtn.io/status"
    r = requests.get(url)
    
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))