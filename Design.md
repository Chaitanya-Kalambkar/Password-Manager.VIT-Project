# Design Documentation

## 1. Problem Statement

See [statement.md](../statement.md) for the full problem statement, scope,
target users and high-level features.

## 2. Objectives

- Provide a way to generate strong, and completely randomly generated passwords without relying on an
  external service or library like 'pip'
- Demonstrating basic encryption/decryption concepts using ASCII encryption, encrypting the stored
  passwords with a key given by the user-chosen master password
- Stores passwords using simple file I/O and a nested dictionary (website -> account/username -> password). Hence the code can support multiple accounts under the same website (e.g. more than one Gmail address under "google")
- Provides a clear, validated, menu interface connecting all of the above statements into one program

## 3. Functional Requirements

| ID | Requirement |
|----|-------------|
| FR1 | The system shall generate a password from a user-specified number of letters, symbols, and numbers. |
| FR2 | The system shall reject a password request where the total requested length is 0. |
| FR3 | The system shall allow the user to store a password against a website name **and** an account/username. |
| FR4 | The system shall encrypt a password before writing it to a .txt file, and decrypt it only when it is retrieved by the user. |
| FR5 | The system shall ask for confirmation before overwriting an existing saved website+account password. |
| FR6 | The system shall allow the user to retrieve, update, delete, and list stored website/account entries. |
| FR7 | The system shall support more than one account/username under the same website using nested dictionaries. |
| FR8 | The system shall persist stored passwords between separate runs of the program. |
| FR9 | The system shall validate and run numeric and text input, and re-prompt the code on invalid input, rather than crashing completely. |

## 4. Non-Functional Requirements

| ID | Category | Requirement |
|----|----------|-------------|
| NFR1 | Security | Passwords will never be written to the .txt file as is, in plain text; rather they are always encrypted first, using a key derived from the master password and then stored further. |
| NFR2 | Usability | The program uses a numbered menu interface which will be easy to understand and will be in plain-language prompts so it can be used without reading documentation. |
| NFR3 | Reliability | Invalid input such as non-numeric answers is caught and re-prompted instead of crashing the program. |
| NFR4 | Maintainability | Functionality is split into single-purpose modules (`generator.py`, `encryption.py`, `storage.py`, `helpers.py`) so each part can be changed independently, which will increase productivity and improve organization. |
| NFR5 | Scalability | The nested dictionary structure (website -> account -> password) allows an unlimited number of accounts per website without any change to the storage format. |

## 5. System Architecture Diagram

```mermaid
flowchart TD
    User(["User"]) --> Main["main.py<br/>menu loop"]
    Main --> Generator["generator.py<br/>generate passwords"]
    Main --> Encryption["encryption.py<br/>encrypt / decrypt"]
    Main --> Helpers["helpers.py<br/>input validation"]
    Main --> Storage["storage.py<br/>save / load"]
    Storage --> DataFile[("passwords_store.txt")]
```

`main.py` is the only module that talks to the other four
support modules using the import function and does the main job.

## 6. Process Flow / Workflow Diagram

```mermaid
flowchart TD
    Start(["Start"]) --> Setup["Enter master password<br/>Derive key<br/>Load saved passwords"]
    Setup --> Menu{"Choose an option (1-7)"}

    Menu -- "1 Generate" --> Gen["Ask website + account<br/>Generate & save password"]
    Menu -- "2 Store" --> Store["Ask website + account<br/>Type or generate, then save"]
    Menu -- "3 Retrieve" --> Retrieve["Ask website + account<br/>Decrypt & show password"]
    Menu -- "4 View" --> View["List saved websites & accounts"]
    Menu -- "5 Delete" --> Delete["Ask website + account<br/>Confirm, then delete"]
    Menu -- "6 Update" --> Update["Ask website + account<br/>Type or generate, then save"]
    Menu -- "7 Exit" --> End(["End"])

    Gen --> Menu
    Store --> Menu
    Retrieve --> Menu
    View --> Menu
    Delete --> Menu
    Update --> Menu
```

## 7. UML Diagrams

### 7.1 Use Case Diagram (simplified)

```mermaid
flowchart LR
    U(["User"])
    U --> UC1(["Generate Password"])
    U --> UC2(["Store Password"])
    U --> UC3(["Retrieve Password"])
    U --> UC4(["View Saved Websites/Accounts"])
    U --> UC5(["Delete Password"])
    U --> UC6(["Update Password"])
```

### 7.2 Component Diagram

This project has no classes - it's plain functions grouped into modules -
so a component diagram (showing modules and what each one exposes) fits
better than a class diagram:

```mermaid
flowchart LR
    subgraph main.py
        M["menu loop"]
    end
    subgraph generator.py
        G["generate_password()<br/>strength_label()"]
    end
    subgraph encryption.py
        E["make_key()<br/>encrypt_password()<br/>decrypt_password()"]
    end
    subgraph storage.py
        S["load_passwords()<br/>save_passwords()"]
    end
    subgraph helpers.py
        H["ask_for_number()<br/>ask_password_settings()<br/>ask_yes_no()<br/>show_accounts()"]
    end

    M --> G
    M --> E
    M --> S
    M --> H
```

### 7.3 Sequence Diagram (Store a Password)

```mermaid
sequenceDiagram
    participant U as User
    participant M as main.py
    participant G as generator.py
    participant E as encryption.py
    participant S as storage.py

    U->>M: Choose "2. Store a password"
    M->>U: Ask for website & account
    U-->>M: website, username

    alt already saved for that website + account
        M->>U: Ask "Overwrite?"
        U-->>M: yes / no
    end

    alt user wants a generated password
        M->>G: generate_password(...)
        G-->>M: new_password
    else user types their own
        U-->>M: new_password
    end

    M->>E: encrypt_password(new_password, key)
    E-->>M: encrypted_password
    M->>S: save_passwords(passwords)
    S-->>M: saved to passwords_store.txt
```

## 8. Storage / Schema Design

There is no database in this project — storage is a nested dictionary
persisted to a text file, which is intentional given the "nothing too
crazy" / no-external-libraries scope of the project. The ER diagram and
schema below describe that structure in database terms anyway, as required.

### 8.1 ER Diagram

```mermaid
erDiagram
    WEBSITE ||--o{ ACCOUNT : has
    WEBSITE {
        string website_name PK
    }
    ACCOUNT {
        string username PK
        string encrypted_password
    }
```

One WEBSITE (e.g. "google") can have many ACCOUNTs (e.g. `a@gmail.com`,
`b@gmail.com`), and each ACCOUNT stores exactly one encrypted password.

### 8.2 Schema Design

**In-memory structure:**

```
passwords = {
    "google": {
        "a@gmail.com": "<encrypted_password_string>",
        "b@gmail.com": "<encrypted_password_string>",
    },
    "netflix": {
        "netflixuser": "<encrypted_password_string>",
    },
}
```

**On-disk format (`passwords_store.txt`)**, one entry per line, with the
website, account/username, and encrypted password separated by a `:::`
delimiter:

```
google:::a@gmail.com:::t&88eUVW
google:::b@gmail.com:::y5)&9*)f
netflix:::netflixuser:::Qz1@92$k
```

| Field | Type | Notes |
|-------|------|-------|
| website | string | stored in lowercase, used as the outer dictionary key |
| account/username | string | the inner dictionary key; lets one website hold several accounts |
| encrypted_password | string | output of `encrypt_password()`; only readable with the correct master password, without it encryption will be jumbled and output password will also be jumbled  |

For backward compatibility, `load_passwords()` can also read older
two-part lines (`website:::encrypted_password`, from before accounts were
added) and files them under the username `"default"`.
