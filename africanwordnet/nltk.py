#!/usr/bin/env python
# African WordNet
#
# Copyright (C) 2020
# Author: Joseph Sefara
# URL: <https://github.com/JosephSefara/AfricanWordNet/>
# For license information, see LICENCE.MD

from nltk.downloader import Downloader


class Helper:
    """
    A set of functions used to extend nltk.
    """

    def __init__(self,):
        """A method to initialize parameters"""

        DEFAULT_URL = 'https://raw.githubusercontent.com/JosephSefara/AfricanWordNet/master/data/index.xml'
        """The default URL for the NLTK data server's index"""

        try:
            downloader = Downloader(server_index_url=DEFAULT_URL)
            downloader.download('africanwordnet')
        except:
            raise
