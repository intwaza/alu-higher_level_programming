#!/usr/bin/python3
"""
Script that takes in a URL and an email address, sends a POST request
"""
import requests
import sys

if __name__ == "__main__":
    email = {'email': sys.argv[2]}
    req = requests.post(sys.argv[1], data=email)
    print(req.text)
