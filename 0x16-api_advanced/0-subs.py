#!/usr/bin/python3
"""
this module contains the function number_of_subscribers
"""

from requests import get


def number_of_subscribers(subreddit):
    """returns the number of subscribers (not active users, total
    subscribers) for a given subreddit."""

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'Python Scripts (by: /u/onohije)'}
    resp = get(url, headers=headers)
    if resp.ok:
        return resp.json().get('data', 0).get('subscribers', 0)
    return 0
