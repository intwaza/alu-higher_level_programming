#!/bin/bash
# Script that takes a URL, sends a request
curl -s "$1" | wc -c
