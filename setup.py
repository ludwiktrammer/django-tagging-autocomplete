# -*- coding: utf-8 -*-
import os
from distutils.core import setup
from distutils.command.install import INSTALL_SCHEMES

long_description = open('README.rst').read()

# install data files where source files are installed
for scheme in INSTALL_SCHEMES.values():
    scheme['data'] = scheme['purelib']

def find_data_files(filepath):
    return sum([
        [(path, [os.path.join(path, name)]) for name in names]
            for path, _, names in os.walk(filepath)], [])

setup(
    name='django-tagging-autocomplete',
    version='0.5.0',
    description='Autocompletion for django-tagging',
    long_description=long_description,
    author='Ludwik Trammer',
    author_email='ludwik@gmail.com',
    url='https://github.com/ludwiktrammer/django-tagging-autocomplete/',
    packages=['tagging_autocomplete'],
    data_files=find_data_files('tagging_autocomplete/static'),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ]
)
