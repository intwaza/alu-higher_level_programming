#!/bin/bash
# Script that sends a GET request with a custom header

curl -s -H "X-HolbertonSchool-User-Id: 98" "$1"
