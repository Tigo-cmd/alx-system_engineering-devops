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
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    header = {
        "User-Agent": "Tigo: Pycharm2023.3.2"
    }

    # response = requests.get(url, headers=header, allow_redirects=False)
    req = requests.get(
        "https://www.reddit.com/r/{}/hot.json".format(subreddit),
        headers={"User-Agent": "Custom"},
        params={"limit": 10},
    )

    if req.status_code == 200:
        for get_data in req.json().get("data").get("children"):
            dat = get_data.get("data")
            title = dat.get("title")
            print(title)
    else:
        print(None)