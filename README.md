# Password Manager

A simple command-line Password Manager written in pure Python, built for the
VITyarthi "Build Your Own Project" submission.

## Overview

This project combines three things into one tool:

1. A **strong password generator** that builds random passwords from a mix
   of letters, numbers and symbols.
2. An **encrypted storage system** that saves passwords for different
   website/account combinations using a basic Caesar-style shift cipher, so
   nothing is stored as plain text.
3. A **menu-driven interface** that lets the user generate, store, retrieve,
   update, delete, and list passwords for different websites and accounts
   (e.g. more than one Gmail account under "google").

## Features

- Generate a random password with a chosen number of letters, symbols and
  numbers
- A simple strength label (Weak / Okay / Strong) shown with each generated
  password
- Store a password for a website **and account/username**, either typed in
  or freshly generated - the same website can have several saved accounts
- Confirmation prompt before overwriting an existing saved website+account
  password
- Retrieve a stored password for a website/account (decrypted on the spot)
- Update or delete a saved password for a specific account
- View a list of every website + account you have saved passwords for
- All passwords are encrypted before being written to disk, using a key
  derived from your own master password
- Input validation: keeps re-asking for numbers until a valid whole number
  is entered, and won't generate an empty password

## Technologies / Tools Used

- Python 3 (standard library only — just `random`)
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

No installation steps beyond having Python itself — there are no external
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

## Notes

- The encryption used here is a basic, educational shift cipher — it is
  meant to demonstrate the concept of encryption/decryption for this
  project, not to provide real-world-grade security.
- `passwords_store.txt` is created next to `main.py` the first time you run
  it, and picks up right where you left off on later runs.
