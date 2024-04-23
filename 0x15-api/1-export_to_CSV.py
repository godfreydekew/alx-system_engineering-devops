#!/usr/bin/python3
"""Saves information about employee into a csv."""
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    usr = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()
    with open("file.csv", "w", encoding="utf-8") as f:
        for todo in todos:
            f.write('"{}","{}","{}","{}"\n'.format(todo.get("userId"), usr.get(
                "username"), todo.get("completed"), todo.get("title")))
