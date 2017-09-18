Sitekey file
=======================

Sitekey file stores all the information required to generate your passwords except the master password you create with passme.

In the sitekey file, sitekey entry is stored as text information as follows.

:: 

 [google]
 hash = sha3_384
 char = an
 len = 14
 seed = GU/Gx=E9Zhvuk+fHny[PQ4iczHcEcc
 comment = '''ID: sekifake
 https://google.com/'''

It is a simple text file and you can edit it with your favorite text editor. Remember that if you change the values of hash, char, len and seed, the sitekey is changed and the password is changed.

As it is a text file, it can be properly managed with version control system such as your private git  repository. Once you lose the sitekey file you can never recover your passwords, so it is recommended to manage the file with a version control system. It does not directly store your passwords for the sites but it is not appropriate to put the file in publicly available location.

Please note that the configuration other than site specific information, such as the filename of the sitekey file, is stored in **.passme** file in your home directory. See more information of **.passme** file at `Configuration <config.rst>`_.

----

Toppage_

.. _Toppage: README.rst
