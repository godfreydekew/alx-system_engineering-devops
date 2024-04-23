#!/usr/bin/python3
"""Saves information about employee into a json file."""
import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()
    all_info = {}
    for user in users:
        my_list = []
        todos = requests.get(
            url + "todos", params={"userId": user.get("id")}).json()
        for todo in todos:
            my_list.append({
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": user.get("username")
            })
        all_info.update({user.get("id"): my_list})
    with open("todo_all_employees.json", "w", encoding="utf-8") as f:
        json.dump(all_info, f)
