import requests
"""
module contains function to get no. of reddit's
subreddit subscribers.
"""


def number_of_subscribers(subreddit):
    """
    Query the Reddit API and fetch data about a subreddit's subscribers.
    """

    headers = {
        "Accept": "*/*",
        "User-Agent": "Student script",
    }

    api_url = 'https://www.reddit.com/r'
    url = '{}/{}/about.json?raw_json=1'.format(api_url, subreddit)
    res = requests.get(url, headers=headers, allow_redirects=False)
    if not res.ok:
        return 0
    data = res.json().get("data")
    subscribers = data.get("subscribers")
    return subscribers

