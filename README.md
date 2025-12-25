# Passme: Password management with command line

**Passme** is a password management tool for the command line. It helps you generate strong, unique passwords for many sites without storing the passwords themselves.

[![en](https://img.shields.io/badge/lang-en-red.svg)](https://github.com/sekika/passme/blob/master/README.md)
[![ja](https://img.shields.io/badge/lang-ja-blue.svg)](https://github.com/sekika/passme/blob/master/README-ja.md)

<img alt="Passme illustration" src="https://sekika.github.io/passme/passme.svg" style="width: min(100%, 600px);  height: auto; margin:auto; display: block" />

Instead of an encrypted vault, Passme generates passwords deterministically every time using a site-specific seed (**sitekey**) stored in a configuration file and a **master password** that only you know.

> **Sitekey + Master password = Password**

**[Read the Full Documentation](https://sekika.github.io/passme/)**

## Key Features

*   **Stateless:** Passwords are calculated on the fly. If you have your sitekey file and your master password, you can generate your passwords anywhere.
*   **Secure:** Offline brute-force attacks are difficult because the attacker cannot verify a guessed password without trying it on the actual login page (unless they already know one of your passwords).
*   **Flexible:** You can customize the length, character set (alphanumeric, symbols, etc.), and hashing algorithm for each site.
*   **Portable:** Includes a feature to generate a standalone [HTML/Javascript file](https://sekika.github.io/passme/passme.html), allowing you to generate passwords on mobile devices without Python.
*   **No Vendor Lock-in:** Uses standard, open algorithms. Even if this software is discontinued, you can recover your passwords using the known calculation logic.

## Installation

Passme requires Python 3.

```bash
pip install passme
```

## Quick Start

### 1. Initialization
Run `passme` to set up your sitekey file location.

```bash
> passme
Filename to save site keys: /path/to/your/sitekeys.txt
```

### 2. Add a Site
Create a new entry for a service (e.g., Google). You can define the character set and length.

```bash
> passme add
Site name: google
Character (an): 
Password length (14): 
...
```

### 3. Generate a Password
To retrieve the password, simply type `passme` followed by the site name.

```bash
> passme google
Master password: [Input your master password]
(Generated password is copied to clipboard)
```

## Security Warning

*   **Do not forget your master password.**
*   **Do not lose your sitekey file.**

Since Passme does not store your passwords, there is no "Forgot Password" recovery mechanism. Losing either your master password or the sitekey file means losing access to all your generated accounts. It is highly recommended to manage your sitekey file in a **private** git repository.

## Documentation

For detailed usage, configuration options, mobile usage (Javascript version), and security details, please refer to the documentation:

[**https://sekika.github.io/passme/**](https://sekika.github.io/passme/)

## History

Since its [public release](https://pypi.org/project/passme/#history) in 2017, the author has migrated from existing password management systems to Passme and has been using it securely through 2025. Currently, over 100 site passwords are managed using this tool.

## License

This software is released under the [MIT License](LICENSE.txt).

Author: [Katsutoshi Seki](https://github.com/sekika)
