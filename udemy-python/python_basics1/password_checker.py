username = input('what is the username? ')
password = input('your password is: ')

# print(f'hello {username} your password is { "*" * len(password)} and it is {len(password)} letters long.')

password_length = len(password)
hidden_password = '*' * password_length

print(f'{username} , your password, {hidden_password}, is {password_length} letters long')

