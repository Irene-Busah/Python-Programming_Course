import random

print('Welcome to Password Generator')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*(),./?=+-123456789'

number = input('Enter the number of passwords you want to generate: ')

number = int(number)

length = input('Your password length: ')
length = int(length)


print('\n Here are your password')

for password in range(number):
    passwords = ''
    for pwd in range(length):
        passwords += random.choice(chars)
    print(passwords)
