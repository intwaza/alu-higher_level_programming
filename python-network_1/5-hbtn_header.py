#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL
"""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]

    req = requests.get(url)
    print(req.headers.get("X-Request-Id"))
