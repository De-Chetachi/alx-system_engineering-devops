#!/usr/bin/python3
'''this module contains a function that queries the reddit api'''
import requests


def recurse(subreddit, hot_list=[], count=0, after=None):
    '''a recursive function queries the reddit api
    arg:    subreddit
            hot_list
    returns a list of all post titles
    if subreddit is invalid return None'''
    # Mozilla/5.0 (Windows NT 10.0; Win64; x64)
    # AppleWebKit/537.36 (KHTML, like Gecko)
    # Chrome/123.0.0.0 Safari/537.36

    header = {
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
            }
    if after is None:
        after = ''
    base_url = 'https://www.reddit.com'
    sr_url = '{}/r/{}/.json?sort={}&limit={}&count={}&after={}'.format(
            base_url, subreddit, 'hot', 50, count, after)

    sr = requests.get(sr_url, headers=header, allow_redirects=False)
    if sr.status_code == 200:
        posts_data = sr.json()['data']['children']
        hot_list.extend(list(map(lambda p: p['data']['title'], posts_data)))
        after = sr.json()['data']['after']
        if len(posts_data) >= 50 and after:
            return recurse(subreddit, hot_list, count + len(posts_data), after)
        else:
            return hot_list if hot_list else None
    else:
        return hot_list if hot_list else None
