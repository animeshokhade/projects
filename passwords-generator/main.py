import random

print('Generate your Password')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*().,?0123456789'

number = int(input('Enter number of Passwords to generate: '))

length = int(input('Input your password length: '))

print('\n Claim your passwords: ')

for pwd in range(number):
    passwords = ''
    for c in range(length): 
        passwords += random.choice(chars)
    print(passwords) 