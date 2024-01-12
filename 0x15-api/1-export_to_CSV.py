#!/usr/bin/python3
"""
script to gather data from an API and
display TODO list progress of an employee.
"""

import requests
import sys
import csv


def fetch_todo_data(employee_id):
    """
    Fetch TODO list data from the given employee ID.
    Args:
        employee_id (int): The ID of the employee.

    Returns:
        dict: TODO list data.
    """
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todo_url = f"{base_url}/todos?userId={employee_id}"

    user_response = requests.get(user_url)
    todo_response = requests.get(todo_url)

    if user_response.status_code != 200:
        print("Error: Unable to fetch user data.")
        sys.exit(1)

    if todo_response.status_code != 200:
        print("Error: Unable to fetch TODO list data.")
        sys.exit(1)

    user_data = user_response.json()
    todo_data = todo_response.json()

    return user_data, todo_data


def display_todo_progress(employee_id, user_data, todo_data):
    """
    Display TODO list progress.
    Args:
        employee_id (int): The ID of the employee.
        user_data (dict): User data.
        todo_data (list): TODO list data.
    """
    employee_name = user_data.get("name")
    total_tasks = len(todo_data)
    completed_tasks = [task for task in todo_data if task.get("completed")]

    print(f"Employee {employee_name} is done with tasks "
          f"({len(completed_tasks)}/{total_tasks}):")

    for task in completed_tasks:
        title = task.get("title")
        print(f"\t {title}")


def export_to_csv(employee_id, user_data, todo_data):
    """
    Export TODO list data to CSV.
    Args:
        employee_id (int): The ID of the employee.
        user_data (dict): User data.
        todo_data (list): TODO list data.
    """
    employee_name = user_data.get("username")
    csv_file_name = f"{employee_id}.csv"

    with open(csv_file_name, mode="w", newline="") as csv_file:
        fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS",
                      "TASK_TITLE"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()

        for task in todo_data:
            writer.writerow({
                "USER_ID": employee_id,
                "USERNAME": employee_name,
                "TASK_COMPLETED_STATUS": str(task.get("completed")),
                "TASK_TITLE": task.get("title")
            })


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    user_data, todo_data = fetch_todo_data(employee_id)
    display_todo_progress(employee_id, user_data, todo_data)
    export_to_csv(employee_id, user_data, todo_data)
