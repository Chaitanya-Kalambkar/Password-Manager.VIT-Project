# Simple tests using plain "assert" statements - no pytest or any
# other library needed. Run this file with:  python test_password_manager.py
# If it finishes and prints "All tests passed!", everything works.

import generator
import encryption
import storage

# ---- Test 1: generate_password returns the correct length ----
password = generator.generate_password(4, 2, 3)
assert len(password) == 9, 'Generated password should be 9 characters long'

# ---- Test 2: generate_password only uses allowed characters ----
allowed_characters = generator.all_letters + generator.numbers + generator.symbols
for character in password:
    assert character in allowed_characters, 'Password contains an unexpected character'

# ---- Test 3: strength_label gives the expected label ----
assert generator.strength_label(2, 1, 1) == 'Weak'
assert generator.strength_label(6, 3, 1) == 'Okay'
assert generator.strength_label(8, 3, 3) == 'Strong'

# ---- Test 4: make_key gives the same key for the same master password ----
key1 = encryption.make_key('hunter22')
key2 = encryption.make_key('hunter22')
assert key1 == key2, 'The same master password should always produce the same key'

# ---- Test 5: encrypting then decrypting gives back the original text ----
key = encryption.make_key('mySecret123')
original = 'Sunshine!99'
encrypted = encryption.encrypt_password(original, key)
decrypted = encryption.decrypt_password(encrypted, key)
assert decrypted == original, 'Decrypting should return the original password'
assert encrypted != original, 'Encrypted password should not look like the original'

# ---- Test 6: save_passwords and load_passwords work together, ----
# ---- including multiple accounts under the same website        ----
# We point storage at a throwaway file so this test never touches
# your real passwords_store.txt.
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
# (test_passwords_store.txt is just leftover test output - safe to delete)

print('All tests passed!')
