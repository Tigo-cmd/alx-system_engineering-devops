#!/usr/bin/python3
"""module  queries the Reddit API and returns the number of subscribers
    (not active users, total subscribers) for a given subreddit."""

import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers (not active users, total subscribers)
        for a given subreddit.
     If an invalid subreddit is given, the function should return 0.
     Args:
         subreddit: subscriber
     """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    header = {
        "User-Agent": "Tigo: Pycharm2023.3.2"
    }
    response = requests.get(url, headers=header, allow_redirects=False)
    if response.status_code == 200:
        result = response.json()
        return result["data"]["subscribers"]
    else:
        return 0
