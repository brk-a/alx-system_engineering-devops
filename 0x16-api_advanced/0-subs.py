#!/usr/bin/python3

"""
returns the number of subscribers for a given subreddit
"""

import requests
import sys


def number_of_subscribers(subreddit):
    """Gets number of subscribers"""
    base_url = 'https://api.reddit.com/r/'
    headers = {'User-Agent': 'my-app/0.0.1'}
    response = requests.get(
        '{}{}/about'.format(
            base_url, subreddit), headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return 0

    about_dict = response.json()

    return about_dict['data']['subscribers']


if __name__ == '__main__':
    number_of_subscribers = __import__('0-subs').number_of_subscribers
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        print("{:d}".format(number_of_subscribers(sys.argv[1])))
