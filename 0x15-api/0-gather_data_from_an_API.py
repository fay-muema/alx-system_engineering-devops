#!/usr/bin/python3
"""Python script that, using this REST API, for a given employee ID, returns information about his/her TODO list progress."""
import requests
import sys

if __name__ == "__main__":
    api_url = "https://jsonplaceholder.typicode.com/"
    response = requests.get(api_url)

    user = '{}users/{}'.format(api_url, sys.argv[1])
    response = requests.get(user)

    json_file = response.json()
    print("Employee {} is done with tasks".format(json_file.get('name')), end="")

    todos = '{}todos?userId={}'.format(api_url, sys.argv[1])
    response = request.get(todos)

    tasks = response.json()

    f_task= []
    for task in tasks:
        if task.get('completed') is True:
            f_task.append(task)

    print("({}/{}):".format(len(f_task), len(tasks)))
    for task in f_task:
        print("\t {}".format(task.get("title")))
