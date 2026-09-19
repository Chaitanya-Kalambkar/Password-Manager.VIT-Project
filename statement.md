# Problem Statement

## Problem Statement

People reuse the same weak passwords across many websites because coming up
with — and remembering — a strong, unique password for every site is
tedious. This leads to accounts being easier to compromise. A simple tool
that can generate strong passwords on demand, and store them securely so
they don't need to be memorized, addresses this problem directly.

## Scope of the Project

This project is a command-line Python application that:

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

- A single individual who wants a lightweight way to generate strong
  passwords and keep track of which password belongs to which
  website/account combination, without relying on a third-party password
  manager service.

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
