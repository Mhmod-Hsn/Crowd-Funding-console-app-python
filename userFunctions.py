import dbHandler
from utils import search
import utils
import globals


def register():

    new_user = {}

    # email
    new_user['email'] = input("Enter your email: ")
    while not utils.check(new_user['email'], 'email'):
        new_user['email'] = input("Enter your email: ")

    # firstname
    new_user['firstname'] = input("Enter your firstname: ")
    while not utils.check(new_user['firstname'], 'text'):
        new_user['firstname'] = input("Enter your firstname: ")

    # lastname
    new_user['lastname'] = input("Enter your lastname: ")
    while not utils.check(new_user['lastname'], 'text'):
        new_user['lastname'] = input("Enter your lastname: ")


    # phone
    new_user['phone'] = input("Enter your phone: ")
    while not utils.check(new_user['phone'], 'phone'):
        new_user['phone'] = input("Enter your phone: ")


    # password
    new_user['password'] = input("Enter your password: ")
    while not new_user['password']:
        new_user['password'] = input("Enter your password: ")


    dbHandler.append_users(new_user)
    return


def login():

    new_user = {}

    # email
    new_user['email'] = input("Enter your email: ")
    while not utils.check(new_user['email'], 'email'):
        new_user['email'] = input("Enter your email: ")

    # password
    new_user['password'] = input("Enter your password: ")
    while not new_user['password']:
        new_user['password'] = input("Enter your password: ")

    found = search(dbHandler.users, new_user['email'], new_user['password'])

    if not found:
        print('Wrong email or password')
        return None

    print('Correct!')
    globals.current_user = found
    print(found)