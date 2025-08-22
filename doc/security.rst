Security
=======================

The master password is not site specific, and therefore you have to remember only one master password. **Do not forget your master password or lose your sitekey file**, because once you lose one of them you will lose all the passwords and you can never recover them (otherwise it is not secure). The sitekey file could be managed with your private git repository.

Algorithm
---------------

Password for a specific site is generated from information in the `sitekey file <sitekey.rst>`_ and **master password** given by a user. In the sitekey file, **hash**, **char**, **len** and **seed** is stored for each site. The algorithm for calculating the password is

* Concatinate the **master password** and **seed**.
* It is hashed with a hash algorithm specified by **hash**.
* It is converted to the string with the characters specified by **char**.
* The string is shortened to the character length specified by **len**.

The calulation routine genpass(seed, hash, char, len) is in `calc.py <../src/passme/calc.py>`_ and you can confirm the algorithm by reading the source code. Note that the first argument in genpass function is the master password and site-specific seed concatinated.

Attacking
---------------

When someone steals your sitekey file, your passwords are not revealed unless the attacker knows the master password. In this situation, the attacker cannot use the offline brute-force attack, because the attacker cannot be sure if the generated password is correct, unless he tries it on site. It is the difference from the most of the other password managers, which stores users password data with encryption.

The offline brute-force attack is available when the attacker has the sitekey file and one known password. In this situation, the attacker can verify the master password by the known password. Once the master password is known the passwords for all the sites are disclosed. The master password should be strong enough to prevent such accident.

This password management system does not prevent all the security issues. For example, the attacker may steal your master password by a keylogger, or steal your site passwords by phishing or stealing clipboard. Therefore general security measure such as not to be affected by malware is always important. As there is always a security risk to some extent, it is advised to use additional security measure such as multi factor authentication when available.

----

Toppage_

.. _Toppage: README.rst
