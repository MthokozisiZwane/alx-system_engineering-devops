#!/usr/bin/python3
"""
A function that querries thereddit api and
returns the number of subscribers for
a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.
    If the subreddit is invalid, returns 0.
    """
    headers = {
            'User-Agent': 'RedditAPIRequest/1.0 (+https://github.\
                    com/MthokozisiZwane)'
            }

    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get('data', {})
        return data.get('subscribers', 0)
    else:
        return 0
