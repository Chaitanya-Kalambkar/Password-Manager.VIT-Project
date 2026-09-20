data_file = 'passwords_store.txt'
delimiter = ':::'   

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
                   
                    website = parts[0]
                    username = 'default'
                    encrypted_password = parts[1]
                else:
                    continue  

                if website not in passwords:
                    passwords[website] = {}
                passwords[website][username] = encrypted_password
        file.close()
    except FileNotFoundError:
        pass  
    return passwords


def save_passwords(passwords):
    file = open(data_file, 'w')
    for website in passwords:
        accounts = passwords[website]
        for username in accounts:
            encrypted_password = accounts[username]
            file.write(website + delimiter + username + delimiter + encrypted_password + '\n')
    file.close()
