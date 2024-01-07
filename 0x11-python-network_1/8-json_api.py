#!/usr/bin/python3
"""
A script that takes in a letter, sends a POST request with the letter as a
parameter, and handles the JSON response appropriately.
"""


import requests
import sys


def search_api(query):
    """
    Sends a POST request with the provided query and processes the JSON
    response.
    """
    url = 'http://0.0.0.0:5000/search_user'
    response = requests.post(url, data={'q': query})

    try:
        result = response.json()
        if result:
            print(f"[{result['id']}] {result['name']}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")


if __name__ == "__main__":
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    search_api(letter)
