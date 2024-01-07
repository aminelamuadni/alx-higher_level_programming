#!/usr/bin/python3
"""
A script that fetches the status from a URL
('https://alx-intranet.hbtn.io/status') using the 'requests' package and
displays the type and content of the body of the response.
"""


import requests


def fetch_status(url):
    """
    Fetches and prints the type and content of the body of the response
    from the given URL.
    """
    response = requests.get(url)
    content = response.text

    print("Body response:")
    print(f"\t- type: {type(content)}")
    print(f"\t- content: {content}")


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    fetch_status(url)
