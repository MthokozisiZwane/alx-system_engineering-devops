#!/usr/bin/python3
"""
A script to gather employee data based on given api
"""


import requests
import sys


def gather_data(employee_id):
    """
    Function to gather data from the API for the given employee ID.
    """
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    try:
        user_response = requests.get(user_url)
        todos_response = requests.get(todos_url)

        # Check for HTTP errors
        if user_response.status_code != 200 or \
           todos_response.status_code != 200:
            print(f"Error: Unable to fetch data. Status codes - "
                  f"User: {user_response.status_code}, "
                  f"Todos: {todos_response.status_code}")
            sys.exit(1)

        user_data = user_response.json()
        todos_data = todos_response.json()

        completed_tasks = [task for task in todos_data if task['completed']]
        total_tasks = len(todos_data)

        print(f"Employee {user_data['name']} is done with tasks "
              f"({len(completed_tasks)}/{total_tasks}):")
        for task in completed_tasks:
            print(f"\t{task['title']}")

    except requests.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    gather_data(employee_id)
