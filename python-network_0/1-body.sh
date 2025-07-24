#!/usr/bin/env bash
# Script that sends a GET request

# Create temporary file to store response body
temp_file=$(mktemp)

# Send request, save body to temp file, and get status code
status_code=$(curl -s -w "%{http_code}" -o "$temp_file" "$1")

# Only display body if status code is 200
if [ "$status_code" -eq 200 ]; then
    cat "$temp_file"
fi

# Clean up temporary file
rm "$temp_file"
