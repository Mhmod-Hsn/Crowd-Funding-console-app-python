import dbHandler
import globals
import utils


def create():
    new_project = {}

    # title
    new_project['title'] = input("Enter your title: ")
    while not utils.check(new_project['title'], 'text'):
        new_project['title'] = input("Enter your title: ")

    # details
    new_project['details'] = input("Enter your details: ")
    while not utils.check(new_project['details'], 'text'):
        new_project['details'] = input("Enter your details: ")

    # target
    new_project['target'] = input("Enter your target: ")
    while not utils.check(new_project['target'], 'p-integer'):
        new_project['target'] = input("Enter your target: ")

    # start
    new_project['start'] = input("Enter your start: ")
    while not utils.check(new_project['start'], 'date'):
        new_project['start'] = input("Enter your start: ")

    # end
    new_project['end'] = input("Enter your end: ")
    while not utils.check(new_project['end'], 'date'):
        new_project['end'] = input("Enter your end: ")

    new_project['author'] = globals.current_user['email']

    dbHandler.append_project(new_project)
    return


def showAll():
    for i in range(len(dbHandler.projects)):
        printProject(dbHandler.projects[i])


def view():
    title = input("Enter your title: ")
    if dbHandler.show_project(title):
        printProject(dbHandler.show_project(title))
    else:
        print("No projects with this name")


def delete():
    title = input("Enter your title: ")
    if dbHandler.delete_project(title):
        printProject(dbHandler.delete_project(title))
    else:
        print("No projects with this name")


def printProject(project):
    print('================================'
          '\ntitle: \t' + project['title'] +
          '\ndetails: \t' + project['details'] +
          '\ntarget: \t' + project['target'] +
          '\nstart: \t' + project['start'] +
          '\nend: \t' + project['end']
          )


def edit():
    title = input("Enter your title: ")
    if dbHandler.show_project(title):
        printProject(dbHandler.show_project(title))
        dbHandler.delete_project(title)
        create()
    else:
        print("No projects with this name or you don't have permission!")


def search():
    # date
    date = input("Enter your date: ")
    while not utils.check(date, 'date'):
        date = input("Enter your date: ")
    matched = dbHandler.search(date)

    for i in range(len(matched)):
        printProject(matched[i])
