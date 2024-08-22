import requests


def get_github_urls():
    return requests.get("https://api.github.com/").json()
