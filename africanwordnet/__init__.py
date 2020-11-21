import os
from .nltk import Helper


name = "africanwordnet"

__version__ = '0.0.1'
__licence__ = 'CC BY-NC-SA 4.0'
__author__ = 'Joseph Sefara'
__url__ = 'https://github.com/JosephSefara/AfricanWordNet/'

PACKAGE_DIR = os.path.dirname(os.path.abspath(__file__))

__all__ = [
    'Helper',
]

Helper()
