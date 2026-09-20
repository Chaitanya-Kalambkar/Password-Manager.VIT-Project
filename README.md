# Password Manager

A simple Password Manager written in pure Python.

## Overview

This project combines three things into one tool:

1. A **strong password generator** that builds random passwords from a mix
   of letters, numbers and symbols, which the user inputs.
2. An **encrypted storage system** that saves passwords for different
   website/account combinations using a basic Caesar-style shift cipher, so
   nothing is stored as plain text.
3. A **menu-driven interface** that lets the user generate, store, retrieve,
   update, delete, and list passwords for different websites and accounts
   (e.g. more than one Gmail account under "google").

## Features

- Generate a random password with a chosen number of letters, symbols and
  numbers, which the user gets to input. 
- A simple strength label (Weak / Okay / Strong) shown with each generated
  password to justify the complexity of the generated password.
- Using dictionaries to store passwords in a key-value pair (and account/username)
  The same website can have several saved accounts as well. 
- Confirmation prompt before overwriting an existing saved website+account
  password.
- Retrieve a stored password for a website/account (decrypted on the spot)
- Update or delete a saved password for a specific account
- View a list of every website + account you have saved passwords for
- All passwords are encrypted before being written to disk, using a key
  derived from your own master password
- Input validation: keeps re-asking for numbers until a valid whole number
  is entered, and won't generate an empty password

## Technologies / Tools Used

- Python 3 (standard library only. just `random` is imported to be used in the password generation)
- No external packages or `pip install` required

## Project Structure

```
password_manager/
├── main.py                     # menu loop - run this file
├── generator.py                # password generation
├── encryption.py               # encrypt / decrypt logic
├── storage.py                  # save / load passwords to disk
├── helpers.py                  # input validation helpers
├── test_password_manager.py    # automated tests
├── README.md
├── statement.md
└── docs/
    └── design.md               # objectives, requirements, diagrams
```

## How to Install & Run

1. Make sure Python 3 is installed.
2. Download/clone this folder so all the `.py` files are together in one
   directory.
3. Open a terminal in that directory (or use VS Code's built-in terminal,
   which starts in the folder you opened) and run:

```
python main.py
```

4. Follow the on-screen menu.

No installation steps beyond having Python itself, as there are no external
dependencies.

## Testing

Automated tests are included in `test_password_manager.py`. They use plain
`assert` statements (no testing library required). To run them:

```
python test_password_manager.py
```

If everything works, it prints `All tests passed!`. The tests cover:

- Generated passwords have the correct length and only use allowed
  characters
- The strength label logic
- Encrypting then decrypting returns the original password
- The same master password always produces the same encryption key
- Saving and loading passwords from disk works correctly, including
  multiple accounts under the same website

You can also test manually by running `main.py` and trying each of the 7
menu options.

## Screenshots

1. <img width="600" height="92" alt="2026-09-20_15-51-46" src="https://github.com/user-attachments/assets/e71f9044-de43-4cbd-a42a-17e961ffefdc" />

2. <img width="1556" height="572" alt="image" src="https://github.com/user-attachments/assets/0145f263-e9e7-43df-8de5-3bc851f23a46" />

3. <img width="693" height="162" alt="Screenshot 2026-09-20 at 3 56 28 PM" src="https://github.com/user-attachments/assets/1df226aa-c463-4d80-b645-ff80291a18d0" />

4. <img width="1494" height="212" alt="image" src="https://github.com/user-attachments/assets/086ea58d-2e29-4154-9189-abc566ef829b" />

5. <img width="894" height="156" alt="image" src="https://github.com/user-attachments/assets/3ca61b77-5642-47a0-86aa-12c7f7a03847" />

6. <img width="1360" height="424" alt="image" src="https://github.com/user-attachments/assets/3cae2ff4-9dc1-4154-ac27-c4b4d8edd4c6" />

7. <img width="880" height="158" alt="image" src="https://github.com/user-attachments/assets/4b13987e-1130-4549-800e-2faae8e987c6" />



## Notes

- The encryption used here is a basic, educational shift cipher and hence it is
  not mainstream secure and only meant to demonstrate the concept of encryption/decryption for this
  project, not to provide real-world-grade security.
- `passwords_store.txt` is created the first time you run
  the `main.py`, and picks up right where you left off on later runs.
- The same master password is required to be entered every time when the `main.py` is ran, otherwise the decryption will not work for the intended stored passwords.  
