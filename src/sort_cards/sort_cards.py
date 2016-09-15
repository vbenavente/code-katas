# -*- coding: utf-8 -*-


def sort_cards(cards):
    """Sort shuffled list of cards, sorted by rank.

    >>> sort_cards(['3', '9', 'A', '5', 'T', '8', '2', '4', 'Q', '7', 'J', '6', 'K'])
    ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']

    """

    new_list = []
    for i, val in enumerate(cards):
        if val == 'A':
            new_val = 1
        elif val == 'T':
            new_val = 10
        elif val == 'J':
            new_val = 11
        elif val == 'Q':
            new_val = 12
        elif val == 'K':
            new_val = 13
        else:
            new_val = int(val)
        (new_list).append(new_val)
    cards = sorted(list(new_list))
    for i, val in enumerate(cards):
        if val == 1:
            cards[i] = 'A'
        elif val == 10:
            cards[i] = 'T'
        elif val == 11:
            cards[i] = 'J'
        elif val == 12:
            cards[i] = 'Q'
        elif val == 13:
            cards[i] = 'K'
        else:
            cards[i] = str(val)
    return cards
