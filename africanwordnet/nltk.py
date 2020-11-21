#!/usr/bin/env python
# African WordNet
#
# Copyright (C) 2020
# Author: Joseph Sefara
# URL: <https://github.com/JosephSefara/AfricanWordNet/>
# For license information, see LICENSE.MD

import nltk


class Helper:
    """
    A set of functions used to extend nltk.
    """

    def __init__(self, **kwargs):
        """
        A method to initialize parameters

        :type random_state: int
        :param random_state: seed
        :type v: bool
        :param v: Verb, default is True
        :type n: bool
        :param n: Noun
        :type runs: int
        :param runs: Number of repetition on single text
        :type p: float, optional
        :param p: The probability of success of an individual trial. (0.1<p<1.0), default is 0.5
        :rtype:   None
        :return:  Constructer do not return.
        """

        # Set random state
        index_url = ''
        # Set verb to be default if no values given
        try:
            if "v" not in kwargs and "n" not in kwargs:
                kwargs['v'] = True
                kwargs['n'] = False
            elif "v" in kwargs and "n" not in kwargs:
                kwargs['v'] = True
                kwargs['n'] = False
            elif "v" not in kwargs and "n" in kwargs:
                kwargs['n'] = True
                kwargs['v'] = False
            if "runs" not in kwargs:
                kwargs['runs']=1

        except KeyError:
            raise

        try:
            if "p" in kwargs:
                if type(kwargs['p']) is not float:
                    raise TypeError("p represent probability of success and must be a float from 0.1 to 0.9. E.g p=0.5")
                elif type(kwargs['p']) is float:
                    self.p = kwargs['p']
            else:
                kwargs['p'] = 0.5  # Set default value
        except KeyError:
            raise

        self.p = kwargs['p']
        self.v = kwargs['v']
        self.n = kwargs['n']
        self.runs = kwargs['runs']

    def geometric(self, data):
        """
        Used to generate Geometric distribution.
        
        :type data: list
        :param data: Input data
        :rtype:   ndarray or scalar
        :return:  Drawn samples from the parameterized Geometric distribution.
        """

        data = np.array(data)
        first_trial = np.random.geometric(p=self.p, size=data.shape[0]) == 1  # Capture success after first trial
        return data[first_trial]

    def replace(self, data):
        """
        The method to replace words with synonyms
        
        :type data: str
        :param data: sentence used for data augmentation
        :rtype:   str
        :return:  The augmented data

        """
        data = data.lower().split()
        data_tokens = [[i, x, y] for i, (x, y) in enumerate(nltk.pos_tag(data))]  # Convert tuple to list
        if self.v:
            for loop in range(self.runs):
                words = [[i, x] for i, x, y in data_tokens if y[0] == 'V']
                words = [i for i in self.geometric(data=words)]  # List of selected words
                if len(words) >= 1:  # There are synonyms
                    for word in words:
                        synonyms1 = wordnet.synsets(word[1], wordnet.VERB)  # Return verbs only
                        synonyms = list(set(chain.from_iterable([syn.lemma_names() for syn in synonyms1])))
                        synonyms_ = []  # Synonyms with no underscores goes here
                        for w in synonyms:
                            if '_' not in w:
                                synonyms_.append(w)  # Remove words with underscores
                        if len(synonyms_) >= 1:
                            synonym = self.geometric(data=synonyms_).tolist()
                            if synonym:  # There is a synonym
                                data[int(word[0])] = synonym[0].lower()  # Take the first success

        if self.n:
            for loop in range(self.runs):
                words = [[i, x] for i, x, y in data_tokens if y[0] == 'N']
                words = [i for i in self.geometric(data=words)]  # List of selected words
                if len(words) >= 1:  # There are synonyms
                    for word in words:
                        synonyms1 = wordnet.synsets(word[1], wordnet.NOUN)  # Return nouns only
                        synonyms = list(set(chain.from_iterable([syn.lemma_names() for syn in synonyms1])))
                        synonyms_ = []  # Synonyms with no underscores goes here
                        for w in synonyms:
                            if '_' not in w:
                                synonyms_.append(w)  # Remove words with underscores
                        if len(synonyms_) >= 1:
                            synonym = self.geometric(data=synonyms_).tolist()
                            if synonym:  # There is a synonym
                                data[int(word[0])] = synonym[0].lower()  # Take the first success

        return " ".join(data)

    def augment(self, data):
        """
        Data augmentation for text. Generate new dataset based on verb/nouns synonyms.
        
        :type data: str
        :param data: sentence used for data augmentation 
        :rtype:   str
        :return:  The augmented data
        """
        # Error handling
        if type(data) is not str:
            raise TypeError("Only strings are supported")
        data = self.replace(data)
        return data 
