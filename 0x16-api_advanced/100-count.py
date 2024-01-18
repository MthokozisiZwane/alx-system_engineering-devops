#!/usr/bin/python3
"""
Recursively queries the Reddit API
"""
import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """
    Recursively queries the Reddit API, parses titles, and prints a sorted
    count of given keywords.
    """
    if counts is None:
        counts = {}

    headers = {'User-Agent': 'RedditAPIRequest/1.0 (+https:\
               //github.com/MthokozisiZwane)'}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    params = {'limit': 100, 'after': after}

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)
        if response.status_code != 200:
            return

        data = response.json().get('data', {}).get('children', [])

        for post in data:
            title = post.get('data', {}).get('title', '').lower()
            for word in word_list:
                word = word.lower()
                if word in title:
                    counts[word] = counts.get(word, 0) + title.count(word)

        after = data[-1].get('data', {}).get('name')
        return count_words(subreddit, word_list, after, counts)
    except Exception as e:
        print(f"Error: {e}")

    # Prints results in descending order by count and alphabetically
    sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    for word, count in sorted_counts:
        print(f"{word}: {count}")
