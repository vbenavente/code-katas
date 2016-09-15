# -*- coding: utf-8 -*-
import pytest
from sort_cards import sort_cards

# Test.assert_equals(sort_cards(list('39A5T824Q7J6K')), list('A23456789TJQK'))
# Test.assert_equals(sort_cards(list('Q286JK395A47T')), list('A23456789TJQK'))
# Test.assert_equals(sort_cards(list('54TQKJ69327A8')), list('A23456789TJQK'))


TEST_SORT_CARDS_DATA = [
    (list('39A5T824Q7J6K'), list('A23456789TJQK')),
    (list('Q286JK395A47T'), list('A23456789TJQK')),
    (list('54TQKJ69327A8'), list('A23456789TJQK')),
]


@pytest.mark.parametrize('a_list, result', TEST_SORT_CARDS_DATA)
def test_sort_cards(a_list, result):
    """Test sort cards method."""
    assert sort_cards(a_list) == result
