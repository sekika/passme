all:

install:
	- python3 -m pip uninstall passme
	python3 -m pip install -e .

test:
	@ cd dev; ./test.sh

deb:
	python3 setup.py --command-packages=stdeb.command bdist_deb
