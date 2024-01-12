#!/usr/bin/python3
"""
Export tasks to CSV format
"""

import csv
import requests
from sys import argv

if __name__ == "__main__":
    user_id = argv[1]
    user_url = f'https://jsonplaceholder.typicode.com/users/{user_id}'
    tasks_url = f'https://jsonplaceholder.typicode.com/todos?userId={user_id}'

    user_response = requests.get(user_url)
    tasks_response = requests.get(tasks_url)

    user_data = user_response.json()
    tasks_data = tasks_response.json()

    username = user_data.get('username')

    csv_filename = f'{user_id}.csv'

    with open(csv_filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS",
                        "TASK_TITLE"])

        for task in tasks_data:
            writer.writerow([user_id, username, task['completed'],
                            task['title']])
