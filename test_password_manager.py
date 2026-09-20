import generator
import encryption
import storage

password = generator.generate_password(4, 2, 3)
assert len(password) == 9, 'Generated password should be 9 characters long'

allowed_characters = generator.all_letters + generator.numbers + generator.symbols
for character in password:
    assert character in allowed_characters, 'Password contains an unexpected character'

assert generator.strength_label(2, 1, 1) == 'Weak'
assert generator.strength_label(6, 3, 1) == 'Okay'
assert generator.strength_label(8, 3, 3) == 'Strong'

key1 = encryption.make_key('hunter22')
key2 = encryption.make_key('hunter22')
assert key1 == key2, 'The same master password should always produce the same key'

key = encryption.make_key('mySecret123')
original = 'Sunshine!99'
encrypted = encryption.encrypt_password(original, key)
decrypted = encryption.decrypt_password(encrypted, key)
assert decrypted == original, 'Decrypting should return the original password'
assert encrypted != original, 'Encrypted password should not look like the original'

storage.data_file = 'test_passwords_store.txt'
sample_passwords = {
    'google': {
        'a@gmail.com': encrypted,
        'b@gmail.com': encryption.encrypt_password('OtherPass1', key),
    }
}
storage.save_passwords(sample_passwords)
loaded_passwords = storage.load_passwords()
assert loaded_passwords == sample_passwords, 'Loaded passwords should match what was saved'
assert len(loaded_passwords['google']) == 2, 'Both accounts under google should be loaded'

print('All tests passed!')
