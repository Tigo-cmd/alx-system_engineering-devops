#!/usr/bin/python3
"""module list containing the titles of all hot articles for a given subreddit."""


from __future__ import annotations
from typing import List, Any
import requests


def recurse(subreddit, hot_list=[], after="") -> list[Any] | None:
    """
    recursive function that queries the Reddit API and returns a list containing the titles of all hot articles for a
    given subreddit. If no results are found for the given subreddit,
    the function should return None.
    :param subreddit: param to be queried
    :param hot_list: list containing the titles of all hot articles for a given subreddit.
    :return: None if no results are found
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    header = {
        "User-Agent": "Tigo: Pycharm2023.3.2"
    }

    response = requests.get(url, headers=header, allow_redirects=False, params={"after": after})
    if requests.status_codes == 200:
        result = response.json()
        data = result["data"]["children"]
        for sub in data[:10]:
            hot_list.append(sub["data"]["title"])
        after = result["data"]["after"]

        if after is None:
            return hot_list
        else:
            recurse(subreddit, hot_list, after)
    else:
        return None
