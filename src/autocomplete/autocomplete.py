#!/usr/bin/env python
# -*- coding: utf-8 -*-
from trie import Trie


class AutoCompleter(object):
    """Python implementation of autocomplete class."""
    def __init__(self, vocabulary, max_completions=5):
        """Initialize the Autocompleter class."""
        self.vocabulary = Trie(iterable=vocabulary)
        self.max_completions = max_completions

    def __call__(self, token):
        """Takes user input and returns list of suggested words, max five."""
        suggested_words = []
        if not isinstance(token, str):
            return suggested_words
        start = self.vocabulary.root
        token = ""
        completions = 0
        while completions < self.max_completions:
            while True:
                if start.keys()[0] != '#':
                    start, token = get_word(start, token)
                else:
                    suggested_words.append(token)
                    break
            return suggested_words
            # try:
            #     start = start[token[completions]]
            #     for k, v in start.items():
            #         if k != '#':
            #             token += k
            #             # while len(start):
            #             #     my_deque.append(start.popitem())
            #             start = start.popitem()
            #             suggested_words.extend(token)
            #             completions += 1
            #             if len(v) > 0:
            #                 start = start[token[completions]]
            #                 suggested_words.append(start.popitem()[0])
            # except KeyError:
            #     return suggested_words
            #
            # return suggested_words


def get_word(start, token):
    k = start.keys()[0]
    token += k
    start = start[k]
    return start, token
