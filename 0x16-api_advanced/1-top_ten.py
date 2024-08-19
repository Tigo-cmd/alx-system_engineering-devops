#!/usr/bin/python3
"""module queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit."""


import json
import requests


def top_ten(subreddit):
    """
    a function that queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit.
    :param subreddit: the subreddit channel
    :return: None and prints None
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    header = {
        "User-Agent": "Tigo: Pycharm2023.3.2"
    }

    response = requests.get(url, headers=header, allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return
    result = response.json().get("data").get("children")
    [print(content.get("data").get("title")) for content in result]