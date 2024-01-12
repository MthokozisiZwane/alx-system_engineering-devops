#!/usr/bin/python3
"""script usng a given api to gather informationm about an employee
"""


import requests as r
import sys

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'
    usr_id = r.get(url + 'users/{}'.format(sys.argv[1])).json()
    to_do = r.get(url + 'todos', params={'userId': sys.argv[1]}).json()
#    print(to_do)
    completed_task = [title.get("title") for title in to_do if
                      title.get('completed') is True]
    print(completed_task)
    print("Employee {} is done with tasks({}/{}):".format(usr_id.get("name"),
                                                          len(completed_task),
                                                          len(to_do)))
    [print("\t {}".format(title)) for title in completed_task]
