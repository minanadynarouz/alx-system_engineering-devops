#!/usr/bin/python3
"""Get employee details from REST API"""

from sys import argv
import requests


def fetch_emp(id):
    """Function to fetch the id from users table and from tasks table"""
    data = ""
    completed = 0
    total_tasks = 0
    tasks_list = []

    if id:
        req_todo = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'.format(id))
        req_user = requests.get('https://jsonplaceholder.typicode.com/users?id={}'.format(id))
        if req_todo.status_code == 200:
            todos = req_todo.json()

    for todo in todos:
        total_tasks += 1
        if todo["completed"]:
            completed += 1
            tasks_list.append(todo["title"])

    user = req_user.json()[0]["name"]

    print("Employee {} is done with tasks({}/{}):".format(user, completed, total_tasks))

    for task in tasks_list:
        print("\t {}".format(task))


if __name__ == '__main__':
        fetch_emp(argv[1])
