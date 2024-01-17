#!/usr/bin/python3
"""
queries the Reddit API and returns a list containing the
titles of all hot articles for a given subreddit
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Returns a list containing the titles of all hot articles for
    a given subreddit.
    If no results are found, returns None.
    """
    headers = {'User-Agent': 'my_user_agent'}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    params = {'limit': 100, 'after': after}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get('data', {}).get('children', [])
        if not data:
            return hot_list
        else:
            titles = [post.get('data', {}).get('title') for post in data]
            hot_list += titles
            after = data[-1].get('data', {}).get('name')
            return recurse(subreddit, hot_list, after)
    else:
        return None
