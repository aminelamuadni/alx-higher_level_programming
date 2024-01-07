#!/usr/bin/python3
"""
A script that takes in a URL and an email address, sends a POST request to the
URL with the email as a parameter, and displays the body of the response.
"""


import urllib.request
import urllib.parse
import sys


def send_post_request(url, email):
    """
    Sends a POST request to the specified URL with the given email and prints
    the response body.
    """
    email_data = urllib.parse.urlencode({'email': email})
    email_data = email_data.encode('ascii')

    with urllib.request.urlopen(url, email_data) as response:
        response_body = response.read().decode('utf-8')
        print(response_body)


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    send_post_request(url, email)
