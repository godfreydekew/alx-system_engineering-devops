#!/usr/bin/python3
"""Saves information about employee into a json file."""
import json
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    usr = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()
    list = []
    for todo in todos:
        list.append({
            "task": todo.get("title"),
            "completed": todo.get("completed"),
            "username": usr.get("username")
        })
    info_dict = {
        "{}".format(sys.argv[1]): list,
    }
    with open("{}.json".format(sys.argv[1]), "w", encoding="utf-8") as f:
        json.dump(info_dict, f)
