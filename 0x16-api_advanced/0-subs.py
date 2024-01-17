#!/usr/bin/python3
"""
querries reddit api for number of subcribers
"""
import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.
    If the subreddit is invalid, returns 0.
    """
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'RedditAPIRequest/1.0 (+https:\
            //github.com/MthokozisiZwane)'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get('data', {})
        return data.get('subscribers', 0)
    else:
        return 0
