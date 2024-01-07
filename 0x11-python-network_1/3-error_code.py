#!/usr/bin/python3
"""
A script that takes in a URL, sends a request to the URL, and displays the
body of the response. In case of HTTP errors, the script prints the error code.
"""


import urllib.request
import urllib.error
import sys


def fetch_url(url):
    """
    Fetches and prints the body of a response from a given URL.
    In case of an HTTP error, prints the error code.
    """
    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as error:
        print(f"Error code: {error.code}")


if __name__ == "__main__":
    url = sys.argv[1]
    fetch_url(url)
