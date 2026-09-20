# The passwords dictionary is TWO levels deep:
#   passwords = {
#       'google': {
#           'someone@gmail.com': '<encrypted password>',
#           'other@gmail.com':   '<encrypted password>',
#       },
#       'instagram': {
#           'someone': '<encrypted password>',
#       },
#   }
# This lets the same website have more than one saved account.

data_file = 'passwords_store.txt'
delimiter = ':::'   # separates website / username / encrypted password on each line


def load_passwords():
    passwords = {}
    try:
        file = open(data_file, 'r')
        for line in file:
            line = line.strip()
            if delimiter in line:
                parts = line.split(delimiter)
                if len(parts) == 3:
                    website = parts[0]
                    username = parts[1]
                    encrypted_password = parts[2]
                elif len(parts) == 2:
                    # Old format from before accounts/usernames were added.
                    # Keep the password, just file it under 'default'.
                    website = parts[0]
                    username = 'default'
                    encrypted_password = parts[1]
                else:
                    continue  # not a line we understand, skip it

                if website not in passwords:
                    passwords[website] = {}
                passwords[website][username] = encrypted_password
        file.close()
    except FileNotFoundError:
        pass  # no saved passwords yet, start with an empty dictionary
    return passwords


def save_passwords(passwords):
    file = open(data_file, 'w')
    for website in passwords:
        accounts = passwords[website]
        for username in accounts:
            encrypted_password = accounts[username]
            file.write(website + delimiter + username + delimiter + encrypted_password + '\n')
    file.close()
