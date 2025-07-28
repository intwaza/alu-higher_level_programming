#!/usr/bin/python3
"""Displays the X-Request-Id header value from a URL response"""
import urllib.request
import sys

with urllib.request.urlopen(sys.argv[1]) as response:
    print(response.headers.get('X-Request-Id'))
