Configuration
=======================

In **.passme** file at your home directory you can set some configurations.

From version 1.1.0, if **.passme** file exists in the current directory, configuration is read from the current directory.

============== ============= ========
Variable       Default value Available values
============== ============= ========
SiteKeyFile
DefaultHash    sha3_384      sha384, sha512, sha3_384, sha3_512 (see note)
ShowMasterPass False         True, False
ShowPass       True          True, False
CopyPass       True          True, False
SeedLen        30
OpenEditor     (none)
VCS            (none)        git
============== ============= ========

* SiteKeyFile is the file name of the site key file.
* DefaulthHash is the hash algorithm to be specified for each site and stored at sitekey file. Please note that sha3_384 and sha3_512 are available from Python 3.6.
* When you set ShowMasterPass True, the master password you type is shown on the terminal. 
* If you set ShowPass True, the password created is shown on the terminal.
* If you set CopyPass True, the password is copied to the clipboard. Please note that is is not available if you are using remote shell.
* SeedLen is the length of the seed for creating password.
* OpenEditor is the command to invoke text editor in your system and can be set with `passme edit <edit.rst>`_.
* If you set VCS git, change of the sitekey file is commited to git repository after **passme add** and the change is reviewed with "git log -p -1" command.

----

Toppage_

.. _Toppage: README.rst
