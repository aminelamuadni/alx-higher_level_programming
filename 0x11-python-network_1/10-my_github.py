#!/usr/bin/python3
"""
A script that takes GitHub credentials (username and personal access token)
and uses the GitHub API to display the user's ID.
"""


import requests
import sys


def fetch_github_id(username, token):
    """
    Fetches and prints the GitHub user ID using the provided username and
    token.
    """
    url = 'https://api.github.com/user'
    response = requests.get(url, auth=(username, token))

    if response.status_code == 200:
        print(response.json().get('id'))
    else:
        print("None")


if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]
    fetch_github_id(username, token)
