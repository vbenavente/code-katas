import forbes


def test_get_forbes_json():
    """Returns json file as a list."""
    forbes_json = forbes.get_forbes_json()
    assert isinstance(forbes_json, list)


def test_create_billionaire_dictionary():
    """Returns age dict with name, networth and industry as value."""
    forbes_json = forbes.get_forbes_json()
    result = forbes.create_billionaire_dictionary(forbes_json)
    assert result["Amancio Ortega"] == (80, 67000000000, 'Zara')


def test_create_filtered_billionaire_list():
    """Returns list of billionaires."""
    forbes_json = forbes.get_forbes_json()
    bill_dict = forbes.create_billionaire_dictionary(forbes_json)
    filtered_list = forbes.create_filtered_billionaire_list(bill_dict)
    assert isinstance(filtered_list, list)
