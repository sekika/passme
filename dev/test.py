#!/usr/bin/env python3
import passme
master = input('Input master password: ')
password = passme.readpass('google', master)
print('Google password: ' + password)
