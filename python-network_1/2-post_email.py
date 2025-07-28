#!/usr/bin/python3
"""Sends a POST request with email parameter"""
import urllib.request
import urllib.parse
import sys

url = sys.argv[1]
email = sys.argv[2]

# Prepare the data for POST request
data = urllib.parse.urlencode({'email': email})
data = data.encode('utf-8')

# Send POST request
with urllib.request.urlopen(url, data=data) as response:
    body = response.read()
    print(body.decode('utf-8'))
