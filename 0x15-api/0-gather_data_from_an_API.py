#!/usr/bin/python3
'''using this REST API, for a given employee ID, returns
information about his/her TODO list progress.'''
import requests
import sys
import json


def get_todo():
    id_ = int(sys.argv[1])
    base_url = 'https://jsonplaceholder.typicode.com'
    user_url = f'{base_url}/users/{id_}'
    todo_url = f'{base_url}/todos?userId={id_}'
    user = requests.get(user_url)
    todo = requests.get(todo_url)

    userInfo = json.loads(user.text)
    todoList = json.loads(todo.text)
    name = userInfo['name']
    done = 0
    notDone = 0

    for task in todoList:
        if task['completed'] is True:
            done += 1
    for task in todoList:
        if task['completed'] is False:
            notDone += 1
    totalTask = done + notDone

    print(f'Employee {name} is done with tasks({done}/{totalTask}):')
    for task in todoList:
        if task['completed'] is True:
            print('\t {}'.format(task['title']))


if __name__ == "__main__":
    get_todo()
