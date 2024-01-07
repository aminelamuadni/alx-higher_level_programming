#!/bin/bash
# This script sends a JSON POST request to a URL with the contents of a file
curl -s -H "Content-Type: application/json" -X POST -d @"$2" "$1"
