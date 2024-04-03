#!/usr/bin/python3
'''this module contains a function that queries the reddit api'''
import requests
import sys


def top_ten(subreddit):
    '''this function queries the reddit api
    arg: subreddit
    prints the titles of the first 10 hot posts listed in the given subreddit
    if subreddit is invalid print None'''
    # Mozilla/5.0 (Windows NT 10.0; Win64; x64)
    # AppleWebKit/537.36 (KHTML, like Gecko)
    # Chrome/123.0.0.0 Safari/537.36

    header = {
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
            }
    base_url = 'https://www.reddit.com'
    sr_url = '{}/r/{}/hot/.json?limit=9'.format(base_url, subreddit)

    sr = requests.get(sr_url, headers=header, allow_redirects=False)
    if sr.status_code == 200:
        sr_data = sr.json()['data']['children']
        for child in sr_data:
            print(child['data']['title'])
    print('None')
