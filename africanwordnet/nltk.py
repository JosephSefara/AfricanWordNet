#!/usr/bin/env python
# African WordNet
#
# Copyright (C) 2020
# Author: Joseph Sefara
# URL: <https://github.com/JosephSefara/AfricanWordNet/>
# For license information, see LICENSE.MD

from nltk.downloader import Downloader


class Helper:
    """
    A set of functions used to extend nltk.
    """

    def __init__(self, **kwargs):
        """
        A method to initialize parameters
        """

        DEFAULT_URL = 'https://raw.githubusercontent.com/JosephSefara/AfricanWordNet/master/index.xml?token=AC3HG3T5T74B3DJHK5PX5KC7YH7HM'
        """The default URL for the NLTK data server's index"""

        try:
            # class ExtendDownloader(Downloader):
            #     def __init__(self):
            #         super().__init__()
            #         self.DEFAULT_URL = DEFAULT_URL
            # downloader = ExtendDownloader()

            downloader = Downloader(server_index_url=DEFAULT_URL)
            downloader.download('african_wordnet')
        except:
            raise
