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
    packages=setuptools.find_packages(exclude=('test*', 'data*')),
    author='Joseph Sefara',
    author_email='sefaratj@gmail.com',
    maintainer="Joseph Sefara",
    maintainer_email="sefaratj@gmail.com",
    license='MIT',
    keywords=['wordnet', 'python', 'natural language processing', 'nlp'],
    url='https://github.com/JosephSefara/AfricanWordNet',
    description='A library for African WordNet.',
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    install_requires=['nltk'],
    python_requires=">=3.5.*",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Human Machine Interfaces",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Text Processing",
        "Topic :: Text Processing :: Filters",
        "Topic :: Text Processing :: General",
        "Topic :: Text Processing :: Indexing",
        "Topic :: Text Processing :: Linguistic",
    ]
)
