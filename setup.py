#!/usr/bin/env python
# -*- coding: utf-8 -*-
import setuptools
import re


def find_version(fname):
    """Attempts to find the version number in the file names fname.
    Raises RuntimeError if not found.
    """
    version = ''
    with open(fname, 'r') as fp:
        reg = re.compile(r'__version__ = [\'"]([^\'"]*)[\'"]')
        for line in fp:
            m = reg.match(line)
            if m:
                version = m.group(1)
                break
    if not version:
        raise RuntimeError('Cannot find version information')
    return version


__version__ = find_version('africanwordnet/__init__.py')


def read(fname):
    with open(fname, "r") as fh:
        content = fh.read()
    return content


setuptools.setup(
      name='africanwordnet',
      version=__version__,
      packages=setuptools.find_packages(exclude=('test*', )),
      author='Joseph Sefara',
      author_email='sefaratj@gmail.com',
      license='CC BY-NC-SA 4.0',
      keywords=['wordnet', 'python', 'natural language processing', 'nlp'],
      url='https://github.com/JosephSefara/AfricanWordNet',
      description='A library for African WordNet.',
      long_description=read("README.md"),
      long_description_content_type="text/markdown",
      install_requires=['nltk'],
      classifiers=[
          "Intended Audience :: Developers",
          "Natural Language :: English",
          "License :: OSI Approved :: CC BY-NC-SA 4.0 License",
          "Operating System :: OS Independent",
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: Implementation :: PyPy",
          "Topic :: Text Processing :: Linguistic",
        ]
)
