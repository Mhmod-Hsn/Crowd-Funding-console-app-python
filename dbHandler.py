import json
import globals
from time import strptime

USERS_FILE = './db/users.json'
PROJECTS_FILE = './db/projects.json'

with open(USERS_FILE) as json_file:
    users = json.load(json_file)


def write_users(data, filename=USERS_FILE):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)


def append_users(data):
    users.append(data)
    write_users(users)


with open(PROJECTS_FILE) as json_file:
    projects = json.load(json_file)


def write_projects(data, filename=PROJECTS_FILE):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)


def append_project(data):
    projects.append(data)
    write_projects(projects)


def show_project(title):
    for i in range(len(projects)):
        if projects[i]['title'] == title:
            return projects[i]
    return False


def delete_project(title):
    for i in range(len(projects)):
        if projects[i]['title'] == title and projects[i]['author'] == globals.current_user['email']:
            del projects[i]
            return write_projects(projects)
    return False


def search(date):
    date = strptime(date, "%d/%m/%Y")

    matched_projects = []

    for i in range(len(projects)):
        start_date = strptime(projects[i]['start'], "%d/%m/%Y")
        end_date = strptime(projects[i]['end'], "%d/%m/%Y")

        if start_date < date < end_date:
            matched_projects.append(projects[i])

    return matched_projects
