#!/bin/bash
# Script that displays all HTTP methods the server will accept

curl -X OPTIONS -I -s "$1" | grep -i "allow:" | cut -d: -f2 | xargs
