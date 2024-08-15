#!/usr/bin/python3
"""module queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit."""


import requests


def top_ten(subreddit):
    """
    a function that queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit.
    :param subreddit: the subreddit channel
    :return: None and prints None
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    header = {
        "User-Agent": "Tigo: Pycharm2023.3.2"
    }

    response = requests.get(url, headers=header, allow_redirects=False)
    try:
        if response.status_code == 200:
            result = response.json()
            titles = result['data']['children']
            for title in titles[:10]:
                print(title["data"]['title'])
        else:
            print(None)
    except requests.exceptions.RequestException:
        print(None)
