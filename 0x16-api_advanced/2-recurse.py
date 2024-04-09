#!/usr/bin/python3
"""
this module contains a recursive function that queries the Reddit API and
returns a list containing the titles of all hot articles for a given subreddit
"""

import requests


def recurse(subreddit, hot_list=[], after=''):
    """
    recursive function that queries the Reddit API and returns a list that
    contains the titles of all hot articles for a given subreddit
    """
    url = 'https://www.reddit.com/r/{}/hot.json?after={}'.format(subreddit, after)
    h = {'User-agent': 'mina'}
    r = requests.get(url, headers=h, allow_redirects=False)

    if r.status_code == 200:
        req = r.json()
        data = req.get('data')
        children = data.get('children')
        for post in children:
            post_data = post.get('data')
            title = post_data.get('title')
            hot_list.append(title)
        after = data.get('after')
        if after is None:
            return hot_list
        else:
            return recurse(subreddit, hot_list, after)
    else:
        return None
