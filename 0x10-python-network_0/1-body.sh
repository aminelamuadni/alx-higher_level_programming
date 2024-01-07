#!/bin/bash
# This script sends a GET request to a URL and displays the body of the response if the status code is 200
curl -s -L "$1" -o response.txt -w '%{http_code}' | grep -q '200' && cat response.txt && rm response.txt
