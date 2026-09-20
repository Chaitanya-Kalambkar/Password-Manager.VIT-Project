import generator
import encryption
import storage
import helpers

print('Welcome to the Password Manager!')
master_password = input('Create/enter your master password: ')
key = encryption.make_key(master_password)
passwords = storage.load_passwords()

while True:
    print('')
    print('What would you like to do?')
    print('1. Generate a new password')
    print('2. Store a password')
    print('3. Retrieve a password')
    print('4. View all saved websites')
    print('5. Delete a saved password')
    print('6. Update a saved password')
    print('7. Exit')
    choice = input('Enter your choice (1-7): ')
    choice = choice.strip()

    if choice == '1':
        website = input('Which website is this password for? (e.g. Instagram, Google, Netflix): ')
        website = website.strip().lower()
        username = input('What is the Gmail account/username this password is for? ')
        username = username.strip()

        if website in passwords and username in passwords[website]:
            overwrite = helpers.ask_yes_no('This website already has a saved password for that account. Overwrite it? (y/n): ')
            if not overwrite:
                print('Cancelled. The old password was kept.')
                continue

        nr_letters, nr_symbols, nr_numbers = helpers.ask_password_settings()
        new_password = generator.generate_password(nr_letters, nr_symbols, nr_numbers)
        label = generator.strength_label(nr_letters, nr_symbols, nr_numbers)
        print('Generated password for ' + username + ' on ' + website + ': ' + new_password + ' (Strength: ' + label + ')')

        encrypted_password = encryption.encrypt_password(new_password, key)
        if website not in passwords:
            passwords[website] = {}
        passwords[website][username] = encrypted_password
        storage.save_passwords(passwords)
        print('Password for ' + username + ' on ' + website + ' has been saved.')

    elif choice == '2':
        website = input('Which website is this password for? (e.g. Instagram, Google, Netflix): ')
        website = website.strip().lower()
        username = input('What is the Gmail account/username this password is for? ')
        username = username.strip()

        if website in passwords and username in passwords[website]:
            overwrite = helpers.ask_yes_no('This website already has a saved password for that account. Overwrite it? (y/n): ')
            if not overwrite:
                print('Cancelled. The old password was kept.')
                continue

        wants_generated = helpers.ask_yes_no('Do you want to generate a new password for it? (y/n): ')

        if wants_generated:
            nr_letters, nr_symbols, nr_numbers = helpers.ask_password_settings()
            new_password = generator.generate_password(nr_letters, nr_symbols, nr_numbers)
            label = generator.strength_label(nr_letters, nr_symbols, nr_numbers)
            print('Generated password: ' + new_password + ' (Strength: ' + label + ')')
        else:
            new_password = input('Type the password you want to store: ')

        encrypted_password = encryption.encrypt_password(new_password, key)
        if website not in passwords:
            passwords[website] = {}
        passwords[website][username] = encrypted_password
        storage.save_passwords(passwords)
        print('Password for ' + username + ' on ' + website + ' has been saved.')

    elif choice == '3':
        website = input('Which website do you want the password for? (e.g. Instagram, Google, Netflix): ')
        website = website.strip().lower()

        if website in passwords:
            helpers.show_accounts(website, passwords)
            username = input('Which account/username do you want the password for? ')
            username = username.strip()

            if username in passwords[website]:
                encrypted_password = passwords[website][username]
                real_password = encryption.decrypt_password(encrypted_password, key)
                print('Password for ' + username + ' on ' + website + ' is: ' + real_password)
            else:
                print('No password saved for ' + username + ' on ' + website)
        else:
            print('No password saved for ' + website)

    elif choice == '4':
        if len(passwords) == 0:
            print('You have no saved passwords yet.')
        else:
            print('Websites and accounts you have saved passwords for:')
            for website in passwords:
                for username in passwords[website]:
                    print('- ' + website + ' (' + username + ')')

    elif choice == '5':
        website = input('Which website do you want to delete from? ')
        website = website.strip().lower()

        if website in passwords:
            helpers.show_accounts(website, passwords)
            username = input('Which account/username do you want to delete? ')
            username = username.strip()

            if username in passwords[website]:
                confirm = helpers.ask_yes_no('Are you sure you want to delete the password for ' + username + ' on ' + website + '? (y/n): ')
                if confirm:
                    del passwords[website][username]
                    if len(passwords[website]) == 0:
                        del passwords[website]
                    storage.save_passwords(passwords)
                    print('Password for ' + username + ' on ' + website + ' has been deleted.')
                else:
                    print('Cancelled. Nothing was deleted.')
            else:
                print('No password saved for ' + username + ' on ' + website)
        else:
            print('No password saved for ' + website)

    elif choice == '6':
        website = input('Which website do you want to update? ')
        website = website.strip().lower()

        if website in passwords:
            helpers.show_accounts(website, passwords)
            username = input('Which account/username do you want to update? ')
            username = username.strip()

            if username in passwords[website]:
                wants_generated = helpers.ask_yes_no('Do you want to generate a new password for it? (y/n): ')

                if wants_generated:
                    nr_letters, nr_symbols, nr_numbers = helpers.ask_password_settings()
                    new_password = generator.generate_password(nr_letters, nr_symbols, nr_numbers)
                    label = generator.strength_label(nr_letters, nr_symbols, nr_numbers)
                    print('Generated password: ' + new_password + ' (Strength: ' + label + ')')
                else:
                    new_password = input('Type the new password: ')

                encrypted_password = encryption.encrypt_password(new_password, key)
                passwords[website][username] = encrypted_password
                storage.save_passwords(passwords)
                print('Password for ' + username + ' on ' + website + ' has been updated.')
            else:
                print('No password saved for ' + username + ' on ' + website + ' yet. Use option 2 to add a new one.')
        else:
            print('No password saved for ' + website + ' yet. Use option 2 to add a new one.')

    elif choice == '7':
        print('Goodbye!')
        break

    else:
        print('Please enter a number from 1 to 7.')
