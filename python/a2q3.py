print('Enter correct username and password combo to continue')
username = input('Enter username: ')
password = input('Enter password: ')
if password=='user' and username=='admin':
    print('Access granted')
else:
    myError = ValueError('Wrong username or password')
    raise myError
        