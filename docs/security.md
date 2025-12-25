---
layout: page
title: Security
permalink: /security/
---

# Security

The master password is not site-specific, meaning you only need to remember one master password for all your accounts. 

**Important:** Do not forget your master password or lose your sitekey file. Once you lose either, you lose all your passwords permanently. There is no recovery mechanism, which is by design to ensure security. It is highly recommended to manage your sitekey file in a secure location, such as a private git repository.

### Algorithm

The password for a specific site is generated from information in the [sitekey file](../sitekey/) combined with the **master password** provided by the user. 

In the sitekey file, the following parameters are stored for each site:
*   **hash**: The hashing algorithm.
*   **char**: The character set.
*   **len**: The length of the password.
*   **seed**: A random seed string.

The algorithm for calculating the password is as follows:

1.  **Concatenate** the master password and the seed.
2.  **Hash** the result using the algorithm specified by `hash`.
3.  **Convert** the hash digest into a string using the characters specified by `char`.
4.  **Shorten** the string to the length specified by `len`.

The calculation routine `genpass(seed, hash, char, len)` can be found in `calc.py` (in the source code), and you are encouraged to review the code to verify the algorithm. Note that in the `genpass` function, the first argument is actually the concatenation of the master password and the site-specific seed.

### Reproducibility and Vendor Independence

Passme utilizes standard, open cryptographic hash algorithms (such as SHA-256) and does not rely on proprietary or hidden logic ("security through obscurity").

This ensures that **your access is future-proof**: even if the Passme software itself becomes unsupported or the project disappears in the future, the password generation logic is transparent and documented. You can reproduce your passwords using a simple script or other tools, as long as you possess your sitekey file and master password. You are never locked into this specific software to retrieve your credentials.

### Attack Vectors

**Theft of Sitekey File:**
If someone steals your sitekey file, your passwords are NOT revealed unless the attacker also knows your master password. In this scenario, an attacker cannot easily perform an offline brute-force attack because they have no way of verifying if a guessed password is correct without trying it on the actual website. This differs from many other password managers that store encrypted password vaults; in those cases, if the encryption is broken, the passwords are revealed.

**Offline Brute-Force Attack:**
An offline brute-force attack becomes possible **only if** the attacker has your sitekey file AND already knows one correct password for one of your sites. In this situation, the attacker can use the known password to verify guesses for your master password. Once the master password is cracked, all other site passwords are compromised. Therefore, your master password should be strong enough to withstand such attacks.

**Other Risks:**
This password management system does not protect against all security issues. For example:
*   An attacker could steal your master password using a **keylogger**.
*   An attacker could steal generated passwords via **phishing** sites or by monitoring your **clipboard**.

General security measures, such as keeping your system free of malware, are always essential. Since no system is risk-free, it is strongly advised to use **Two-Factor Authentication (2FA)** whenever available on the services you use.

---

[Top page](../)
