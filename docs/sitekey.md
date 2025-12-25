---
layout: page
title: Sitekey
permalink: /sitekey/
---

# Sitekey file

The sitekey file stores all the information required to generate your passwords, *except* for the master password (which only you know).

In the sitekey file, each site entry is stored as text in the following format:

```text
[google]
hash = sha3_384
char = an
len = 14
seed = GU/Gx=E9Zhvuk+fHny[PQ4iczHcEcc
comment = '''ID: sekifake
https://google.com/'''
```

It is a simple text file, so you can edit it with your favorite text editor. 

**Warning:** If you change the values of `hash`, `char`, `len`, or `seed`, the sitekey changes, and consequently, the generated password will change.

### Management

Since it is a text file, it can be easily managed with a version control system like a **private** git repository. 

*   **Backup:** If you lose the sitekey file, you can never recover your passwords. Therefore, version control acts as a crucial backup.
*   **Privacy:** While the file does not directly store your passwords, it contains half of the "key" (the seed). It is not appropriate to place this file in a publicly available location (like a public GitHub repository).

### Configuration location

Please note that general configurations (non-site-specific settings), such as the location/filename of the sitekey file itself, are stored in a separate `.passme` file in your home directory. See [Configuration](../config/) for more details.

---

[Top page](../)
