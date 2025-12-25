---
layout: page
title: Add
permalink: /add/
---

# Passme add command

You can create a sitekey for a new site using the `passme add` command as follows:

```bash
> passme add
Site name: google
Character (an): 
Password length (14): 
Comment (no input to finish): ID: sekifake
Comment (no input to finish): https://google.com/
Comment (no input to finish): 

New sitekey for google was written in (filename of the sitekey file) as
hash = sha3_384, char = an, len = 14, seed = GU/Gx=E9Zhvuk+fHny[PQ4iczHcEcc
```

First, you enter the **site name**. Then, you will be prompted to input the **characters** to use and the **password length**. If you simply press **Enter**, the default values are selected. In this example, the default values of *an* (alphanumeric) and *14* (length) are selected. If you change these values, they will become the default values for the next time.

Here is a list of character types that can be selected:

| Char | Explanation |
| :--- | :--- |
| a | Alphabet (A-Z, a-z) |
| n | Numeric (0-9) |
| an | Alphabet and numeric |
| ans | Alphabet, numeric, and symbols (`+/#[$-=?@]_!`) |
| ans95 | All 95 available ASCII characters |

**Note:** `ans95` is not available in the [Javascript version](../javascript/).

You can also add site-specific information as comments, such as your user ID, the URL of the login page, or any other notes. UTF-8 characters can be used in the comments. You can input multiple comment lines; press Enter on an empty line to finish.

The example above will create a sitekey entry for `google` in the [sitekey file](../sitekey/).

---

[Top page](../)