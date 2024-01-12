print('Enter your name')
name = input()
print('Enter your password')
password = input()
if name == 'Mary':
    print('Hello, Mary')
    if password == 'swordfish':
        print('Acess granted.')
    else:
        print('Wrong password.') 
else:
    print('Hello, stranger.')