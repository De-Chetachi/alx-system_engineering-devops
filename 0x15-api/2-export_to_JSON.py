#!/usr/bin/python3
'''using this REST API, for a given employee ID, returns
information jk about his/her TODO list progress.'''
import csv
import json
import requests
import sys


def get_todo(id_):
    # id_ = int(sys.argv[1])
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


def export_to_csv(id_):
    '''export data in the CSV format'''
    base_url = 'https://jsonplaceholder.typicode.com'
    user_url = f'{base_url}/users/{id_}'
    todo_url = f'{base_url}/todos?userId={id_}'
    user = requests.get(user_url).json()
    username = user['username']
    tasks = requests.get(todo_url).json()
    list_ = []
    for task in tasks:
        title = task["title"]
        status = task["completed"]
        inner_list = [id_, username, status, title]
        list_.append(inner_list)
    with open(f'{id_}.csv', 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for data in list_:
            csv_writer.writerow(data)


def export_to_json(id_):
    '''export data from an api to a json file'''
    base_url = 'https://jsonplaceholder.typicode.com'
    user_url = f'{base_url}/users/{id_}'
    todo_url = f'{base_url}/todos?userId={id_}'
    user = requests.get(user_url).json()
    username = user['username']
    tasks = requests.get(todo_url).json()
    dict_ = {}
    list_ = []
    for task in tasks:
        title = task["title"]
        status = task["completed"]
        dict_in_list = {}
        dict_in_list["task"] = title
        dict_in_list["completed"] = status
        dict_in_list["username"] = username
        list_.append(dict_in_list)
    dict_[f"{id_}"] = list_
    with open(f'{id_}.json', 'w') as json_file:
        json.dump(dict_, json_file)


if __name__ == "__main__":
    id_ = int(sys.argv[1])
    export_to_json(id_)
