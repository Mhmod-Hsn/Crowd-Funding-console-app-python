import userFunctions
import projectFunctions
import globals


def printMenu():

    print('\n\n\n\n'
          '================================\n '
          '              MENU\n '
          '================================\n'
          '1 - Register\n'
          '2 - Login\n'
          '================================\n'
          '3 - Create project\n'
          '4 - View projects\n'
          '5 - read project\n'
          '6 - delete project\n'
          '7 - edit project\n'
          '8 - search for a project\n'

          '================================\n'
          '9 - Exit\n'
          '================================\n'
          'Enter a choice and press enter => '
          )

    user_input = 0

    while user_input != 9:

        user_input = int(input())

        if user_input == 1:
            userFunctions.register()
            printMenu()

        elif user_input == 2:
            userFunctions.login()
            printMenu()

        elif user_input == 3:
            if globals.check_login():
                projectFunctions.create()
            printMenu()

        elif user_input == 4:
            if globals.check_login():
                projectFunctions.showAll()
            printMenu()

        elif user_input == 5:
            if globals.check_login():
                projectFunctions.view()
            printMenu()

        elif user_input == 6:
            if globals.check_login():
                projectFunctions.delete()
            printMenu()

        elif user_input == 7:
            if globals.check_login():
                projectFunctions.edit()
            printMenu()

        elif user_input == 8:
            # if globals.check_login():
            projectFunctions.search()
            printMenu()

        elif user_input == 9:
            print('Exiting...')


