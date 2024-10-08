# Passme

Passme is a password management tool with command line or web browzer. It helps you generate strong passwords for many sites. It generates password every time from a site-specific seed (sitekey) stored in the configuration file (sitekey file) and a master password that you memorize and type every time.

## Features

- Easy to use from command line. Best fit for programmers.
- HTML file can be created to generate the passwords from your mobile devices.
- Site-specific seeds are stored in a single text file and can be managed easily.

## Basic usage

```
> passme google
Master password: (input master password)
OT9BD5h6cHmWlN
Password copied to clipboard.
```

## Use as a Python library

```
import passme
master = input('Input master password: ')
password = passme.readpass('google', master)
print('Google password: ' + password)
```

## Full document

- See [full document](https://github.com/sekika/passme/blob/master/doc/README.rst)
- [Tutorial movie](https://youtu.be/6DXPhyYhYsE)
