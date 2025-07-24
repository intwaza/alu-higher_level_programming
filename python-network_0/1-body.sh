#!/bin/bash
# Script that sends a GET request and displays body only for 200 status code responses
[ "$(curl -s -L -w "%{http_code}" -o /tmp/body "$1")" = "200" ] && cat /tmp/body; rm -f /tmp/body