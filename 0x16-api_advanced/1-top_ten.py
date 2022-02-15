#!/usr/bin/python3

"""
prints top ten hot posts for a given subreddit
"""

import requests
import sys


def top_ten(subreddit):
    """Gets top ten posts in subreddit"""
    base_url = 'https://api.reddit.com/r/'
    headers = {'User-Agent': 'my-app/0.0.1'}
    response = requests.get(
        '{}{}/hot?limit=10'.format(
            base_url, subreddit), headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print('None')
    else:
        hot_dict = response.json()
        if len(hot_dict['data']['children']) == 0:
            print('None')
        else:
            for d in hot_dict['data']['children']:
                print(d['data']['title'])


if __name__ == '__main__':
    top_ten = __import__('1-top_ten').top_ten
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])
