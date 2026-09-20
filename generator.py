import random

lowercase_letters = list('abcdefghijklmnopqrstuvwxyz')
uppercase_letters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
numbers = list('0123456789')
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

all_letters = lowercase_letters + uppercase_letters


def generate_password(nr_letters, nr_symbols, nr_numbers):
    password_characters = []

    for i in range(nr_letters):
        password_characters.append(random.choice(all_letters))

    for i in range(nr_symbols):
        password_characters.append(random.choice(symbols))

    for i in range(nr_numbers):
        password_characters.append(random.choice(numbers))

    random.shuffle(password_characters)

    password = ''
    for character in password_characters:
        password = password + character

    return password


def strength_label(nr_letters, nr_symbols, nr_numbers):
    
    total = nr_letters + nr_symbols + nr_numbers
    if total < 8:
        return 'Weak'
    elif total < 12:
        return 'Okay'
    else:
        return 'Strong'
