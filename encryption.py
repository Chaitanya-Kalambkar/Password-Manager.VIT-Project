
lowest_code = 32    
highest_code = 126  
total_codes = highest_code - lowest_code + 1  


def make_key(master_password):
    total = 0
    for character in master_password:
        total = total + ord(character)
    key = total % total_codes
    return key


def encrypt_password(password, key):
    encrypted_password = ''
    for character in password:
        code = ord(character) - lowest_code
        code = code + key
        code = code % total_codes
        code = code + lowest_code
        encrypted_password = encrypted_password + chr(code)
    return encrypted_password


def decrypt_password(encrypted_password, key):
    decrypted_password = ''
    for character in encrypted_password:
        code = ord(character) - lowest_code
        code = code - key
        code = code % total_codes
        code = code + lowest_code
        decrypted_password = decrypted_password + chr(code)
    return decrypted_password
