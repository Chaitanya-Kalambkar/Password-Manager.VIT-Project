# Problem Statement

## Problem Statement

Personally I've seen my own mother tediously trying to come up with strong passwords for all her accounts and apps, and then writing them in old diaries for later use, hence people reuse the same weak passwords across many websites because coming up with, and remembering a strong, unique password for every site is tedious. This leads to accounts being easier to hack into as passwords are easy to guess. So a simple tool that can generate strong passwords, and store them and do encryption/decryption all securely inside one's computer addresses this problem directly.

## Scope of the Project

This project is a Python application that:

- Generates random passwords made up of letters, numbers and symbols
- Encrypts passwords before saving them to disk, and decrypts them on
  request
- Lets the user store, retrieve, update, delete, and list passwords by
  website **and account/username**, so the same website (e.g. Google) can
  have more than one saved account

It does **not** cover: browser integration, cloud syncing, multi-user
accounts, or production-grade cryptography. It is a self-contained,
single-user, local command-line tool.

## Target Users

- A single individual who wants a easy to use and seamless way to generate strong
  passwords and keep track of which password belongs to which
  website/account combination, without relying on a third-party password
  manager service. For certain people this may be better than google's password manager because that can get leaked in a data breach in the main server of google, but this      tool runs locally in one's computer.  

## High-Level Features

1. Generate a random password with a chosen mix of letters, symbols and
   numbers, with a quick strength indicator
2. Store a password (typed or generated) for a named website and
   account/username, encrypted before being saved
3. Retrieve a stored password for a website/account, decrypted using the
   master password
4. View all website + account combinations that have a saved password
5. Update or delete a saved password for a specific account
6. Support multiple accounts under the same website (e.g. two different
   Gmail addresses under "google")
