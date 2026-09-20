def ask_for_number(prompt_text):
    
    while True:
        text = input(prompt_text)
        try:
            number = int(text)
            return number
        except ValueError:
            print('That is not a whole number. Please try again.')


def ask_password_settings():
   
    while True:
        nr_letters = ask_for_number('How many letters would you like? ')
        nr_symbols = ask_for_number('How many symbols would you like? ')
        nr_numbers = ask_for_number('How many numbers would you like? ')
        total = nr_letters + nr_symbols + nr_numbers
        if total > 0:
            return nr_letters, nr_symbols, nr_numbers
        else:
            print('Your password needs at least 1 character in total. Please try again.')


def ask_yes_no(prompt_text):
    answer = input(prompt_text)
    answer = answer.strip().lower()
    return answer == 'y'


def show_accounts(website, passwords):
    
    print('Saved accounts for ' + website + ':')
    for username in passwords[website]:
        print('- ' + username)
