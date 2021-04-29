import re

regex = {
    'email': '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$',
    'text': '[a-zA-Z]',
    'password': '/(?=(.*[0-9]))((?=.*[A-Za-z0-9])(?=.*[A-Z])(?=.*[a-z]))^.{3,}$',
    'phone': '^01[0125][0-9]{8}$',
    'p-integer': '^[+]?[0-9]+$',
    'n-integer': '^[-]?[0-9]+$',
    'date': '^(((0[1-9]|[12]\d|3[01])\/(0[13578]|1[02])\/((19|[2-9]\d)\d{2}))|((0[1-9]|[12]\d|30)\/(0[13456789]|1[012])\/((19|[2-9]\d)\d{2}))|((0[1-9]|1\d|2[0-8])\/02\/((19|[2-9]\d)\d{2}))|(29\/02\/((1[6-9]|[2-9]\d)(0[48]|[2468][048]|[13579][26])|((16|[2468][048]|[3579][26])00))))|^(0[1-9]|1[012])[- /.](0[1-9]|[12][0-9]|3[01])[- /.](19|20)\d\d+$',
}


def search(search_list, email, password):
    for i in range(len(search_list)):
        if search_list[i]['email'] == email and search_list[i]['password'] == password:
            return search_list[i]
    return False


def check(value, input_type):
    # pass the regular expression
    # and the string in search() method
    return re.search(regex[input_type], value)
