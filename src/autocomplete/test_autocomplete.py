import autocomplete


def test_autocomplete():
    """Tests that a list of options is returned."""
    vocabulary = ['fix', 'fax', 'fit', 'fist', 'full', 'finch', 'final', 'finial']
    complete_me = autocomplete.AutoCompleter(vocabulary, max_completions=4)
    suggested_words = complete_me('fi')
    assert isinstance(suggested_words, list)
