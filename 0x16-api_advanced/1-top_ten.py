#!/usr/bin/python3
"""
returns hottest posts of a subreddit
"""
import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts for a given subreddit.
    If the subreddit is invalid, prints None.
    """
    headers = {'User-Agent': 'RedditAPIRequest/1.0 (+https:\
            //github.com/MthokozisiZwane)'}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    params = {'limit': 10}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get('data', {}).get('children', [])
        for post in data:
            print(post.get('data', {}).get('title'))
    else:
        print(None)
