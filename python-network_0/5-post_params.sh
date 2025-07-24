#!/usr/bin/env bash
# Script that sends a POST request with parameters and displays the response body

curl -s -d "email=test@gmail.com" -d "subject=I will always be here for PLD" "$1"
