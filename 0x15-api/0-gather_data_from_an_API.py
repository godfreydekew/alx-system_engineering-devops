#!/usr/bin/python3
"""Makes a get request from api and print employee information"""
import json
import requests
import sys


if __name__ == '__main__':
    """urls for each api call"""
    usr_id = int(sys.argv[1])
    url = 'https://jsonplaceholder.typicode.com/todos'
    user_url = f'https://jsonplaceholder.typicode.com/users/{usr_id}/'
    data = requests.get(url).json()
    count = 0
    done_t = 0
    titles = []
    usr = requests.get(user_url).json()
    for item in data:
        if item.get('userId') == usr_id:
            count += 1
            if item.get('completed') is True:
                titles.append(item.get('title'))
                done_t += 1
    print(f"Employee {usr.get('name')} is done with tasks({done_t}/{count}):")
    for title in titles:
        print('\t {}'.format(title))
