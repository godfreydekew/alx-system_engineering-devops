#!/usr/bin/python3
import requests


def number_of_subscribers(subreddit):
    """
    This function returns the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
    """

    url = f"https://api.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "My Reddit Subscriber Counter v1.0"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        subscribers = data["data"]["subscribers"]
        return subscribers
    else:
        return 0
