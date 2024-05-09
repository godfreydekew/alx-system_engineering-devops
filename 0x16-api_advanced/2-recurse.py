#!/usr/bin/python3
"""Uses recursion to get all the titles of hot topics"""
import requests


def recurse(subreddit, hot_list=[], after=''):
    """
    Creates a list of hot lists of given subreddit

    args:
        subreddit (str): name of subreddit
        hot_list (list): list of hot topics
        after (str): after parameter for url

    returns:
        str: None if url is not valid
        list: list of hot topics
    """

    if after:
        url = 'https://www.reddit.com/r/{}/hot.json?after={}'.format(
                subreddit, after)
    else:
        url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'MyReddit/v1.0'}
    response = requests.get(
        url,
        headers=headers,
        allow_redirects=False,
    )

    if response.status_code == 404:
        return
    else:
        for info_dict in response.json().get("data").get("children"):
            hot_list.append(info_dict.get("data").get("title"))
        if response.json().get("data").get("after") is not None:
            recurse(subreddit, hot_list, after=response.json().get(
                "data").get("after"))
        return hot_list
