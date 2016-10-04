import autocomplete


def test_get_word_token():
    """Tests that a word is returned as the token."""
    vocabulary = ['fix', 'fax', 'fit', 'fist', 'full', 'finch', 'final', 'finial']
    start = autocomplete.AutoCompleter(vocabulary, max_completions=5)
    start = start.vocabulary.root
    token = ''
    start, token = autocomplete.get_word(start, token)
    assert isinstance(token, str)


def test_get_word_start():
    """Tests that an ordered dictionary is returned as start."""
    vocabulary = ['fix', 'fax', 'fit', 'fist', 'full', 'finch', 'final', 'finial']
    start = autocomplete.AutoCompleter(vocabulary, max_completions=5)
    start = start.vocabulary.root
    token = ''
    start, token = autocomplete.get_word(start, token)
    assert isinstance(start, dict)
