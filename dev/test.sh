#!/bin/sh
# Change to this directory
cd `echo $0 | sed -e 's/[^/]*$//'`
passme list
passme twitter test
echo 'flake8'
flake8 ../passme/*.py | sed -e 's/^.*passme\///' | grep -v E501
