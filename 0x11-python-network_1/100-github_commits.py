#!/usr/bin/python3
"""
A script that lists the last 10 commits of a given repository from a specific
user on GitHub. The commits are printed in the format '<sha>: <author name>'.
"""


import requests
import sys


def list_commits(repo_name, owner):
    """
    Lists the last 10 commits of the specified repository from the given owner.
    """
    url = f'https://api.github.com/repos/{owner}/{repo_name}/commits'
    response = requests.get(url)

    if response.status_code == 200:
        commits = response.json()[:10]
        for commit in commits:
            sha = commit.get('sha')
            author_name = commit.get('commit').get('author').get('name')
            print(f"{sha}: {author_name}")


if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner = sys.argv[2]
    list_commits(repo_name, owner)
