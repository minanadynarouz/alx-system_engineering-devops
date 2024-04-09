#!/usr/bin/python3
"""
this module contains a function that queries the Reddit API and returns the
number of subscribers for a given subreddit, if an invalid subreddit is
given, the function should return 0
"""

import requests


def number_of_subscribers(subreddit):
    """
    queries the Reddit API and returns number of subscribers for a given
    subreddit
    """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    h = {'User-agent': 'mina'}
    r = requests.get(url, headers=h, allow_redirects=False)

    if r.status_code == 200:
        req = r.json()
        info = req.get('data')
        subscribers = info.get('subscribers')
        if info is not None and subscribers is not None:
            return subscribers
    return 0
