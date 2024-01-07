#!/bin/bash
# This script sends a request to a specific endpoint that responds with "You got me!"
curl -sLX PUT 0.0.0.0:5000/catch_me -H "origin: HolbertonSchool" -d "user_id=98"
