#!/usr/bin/python3

"""
prints top ten hot posts for a given subreddit
"""

import requests
import sys


def recurse(subreddit, hot_list=[], after=''):
    """Gets hot posts in subreddit"""
    base_url = 'https://api.reddit.com/r/'
    headers = {'User-Agent': 'my-app/0.0.1'}
    response = requests.get(
        '{}{}/hot?after={}'.format(
            base_url,
            subreddit, after), headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return None
    else:
        hot_dict = response.json()
        if len(hot_dict['data']['children']) == 0:
            return hot_list
        else:
            for d in hot_dict['data']['children']:
                hot_list.append(d['data']['title'])

            after = hot_dict['data']['after']
            if after is None:
                return hot_list
            return recurse(subreddit, hot_list, after=after)


if __name__ == '__main__':
    recurse = __import__('2-recurse').recurse
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        result = recurse(sys.argv[1])
        if result is not None:
            print(len(result))
        else:
            print("None")
