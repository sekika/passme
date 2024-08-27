#!/bin/sh
# Change to this directory
cd `echo $0 | sed -e 's/[^/]*$//'`
echo '=== test'
passme test

echo '=== autopep8'
autopep8 -i --aggressive ../src/passme/*.py

echo '=== mypy'
mypy ../src/passme/*.py

echo '=== flake8'
flake8 --ignore=E501 ../src/passme/*.py
