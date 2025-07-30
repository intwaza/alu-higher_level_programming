#!/usr/bin/python3
"""Sends a POST request with email parameter"""
import urllib.request
import urllib.parse
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    email = argv[2]
    content = urllib.parse.urlencode({'email': email}).encode('utf-8')
    req = urllib.request.Request(url, data=content, method='POST')
    with urllib.request.urlopen(req) as response:
        content = response.read().decode('utf-8')
        print(content)
