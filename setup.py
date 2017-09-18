# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='passme',
    version='0.1.1',
    description='Password management with command line',
    long_description=long_description,
    url='https://github.com/sekika/passme',
    author='Katsutoshi Seki',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: End Users/Desktop',
        'Topic :: Security',
        'Topic :: Security :: Cryptography',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='password',
    packages=['passme'],
    install_requires=['ConfigObj', 'clipboard'],
    python_requires=">=3.4",
    entry_points={  
        'console_scripts':  
            'passme = passme.main:main'  
    },
)
