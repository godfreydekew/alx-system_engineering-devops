#!/usr/bin/python3
""" prints the titles of the first 10 hot posts listed for a given subreddit"""
import requests


def top_ten(subreddit):
    """
    Print top 10 hot topics

    args:
        subreddit (str): name of subreddit

    returns:
        str: None if url is not valid
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'MyReddit/v1.0'}
    params = {"limit": 10}
    response = requests.get(
        url,
        headers=headers,
        allow_redirects=False,
        params=params
    )
    if response.status_code == 404:
        print(None)
        return
    else:
        for info_dict in response.json().get("data").get("children"):
            print("{}".format(info_dict.get("data").get("title")))
