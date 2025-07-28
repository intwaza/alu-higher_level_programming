#!/usr/bin/env python3
"""
Script that takes GitHub credentials (username and password) and uses 
the GitHub API to display your id using Basic Authentication.
"""
import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    
    url = "https://api.github.com/user"
    r = requests.get(url, auth=(username, password))
    
    if r.status_code == 200:
        user_data = r.json()
        print(user_data.get('id'))
    else:
        print("None")
