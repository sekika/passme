#!/bin/sh
# Change to this directory
cd `echo $0 | sed -e 's/[^/]*$//'`
echo 'flake8'
flake8 ../passme/*.py | sed -e 's/^.*passme\///' | grep -v E501
passme test
