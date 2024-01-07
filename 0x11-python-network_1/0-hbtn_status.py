#!/usr/bin/python3
"""
A script to fetch and display the status from a URL using the urllib package.
This script demonstrates basic network programming concepts like making an HTTP
GET request and handling the response in Python.
"""


import urllib.request


def fetch_status(url):
    """
    Fetches the status from a given URL using urllib and prints the response
    content, its type, and the UTF-8 decoded content.
    """
    with urllib.request.Request(url) as response:
        content = response.read()

        print("Body response:")
        print(f"\t- type: {type(content)}")
        print(f"\t- content: {content}")
        print(f"\t- utf8 content: {content.decode('utf-8')}")

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    fetch_status(url)
