current_user = None


def check_login():
    if current_user:
        return True
    else:
        print('Login first')
        return False
