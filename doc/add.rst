Passme add command
=======================

You can create a sitekey for a new site by **passme add** as follows.

.. code-block:: bash

 > passme add
 Site name: google
 Character (an): 
 Password length (14): 
 Comment (no input to finish): ID: sekifake
 Comment (no input to finish): https://google.com/
 Comment (no input to finish): 
 
 New sitekey for google was written in (filename of the sitekey file) as
 hash = sha3_384, char = an, len = 14, seed = GU/Gx=E9Zhvuk+fHny[PQ4iczHcEcc

First you enter the site name. Then you will be prompted to input the chracters to use and password length. If you just type return default values are selected. In this example default values of *an* and *14* are selected. If you change the values it will be default value for the next time. Here is a list of character types that can be selected.

===== ==========
Char  Explanation
===== ==========
a     Alphabet (A-Z, a-z)
n     Numeric (0123456789)
an    Alphabet and numeric
ans   Alphabet, numeric and +/#[$-=?@]_!
ans95 All of 95 available ASCII characters
===== ==========

Please note that ans95 is not available in `Javascript version <javascript.rst>`_. You can also add site specific information as comments, for example, your user ID, URL of the login page and whatever. UTF-8 characters can be used in the comment. You can input multiple comments.

The above example will create a sitekey entry of google in the `sitekey file <sitekey.rst>`_.

----

Toppage_

.. _Toppage: README.rst
