# Every character on the keyboard has a number behind the scenes,
# called its ASCII code (for example, "A" is 65, "a" is 97).
# We shift that number by a secret amount ("key") to scramble the
# text, and shift it back by the same amount to unscramble it.
# The key comes from the master password, so only someone who
# knows the master password can turn the scrambled text back into
# the real password.

lowest_code = 32     # ASCII code of the space character
highest_code = 126   # ASCII code of the "~" character
total_codes = highest_code - lowest_code + 1   # how many characters we shift between


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
