# -*- coding: utf-8 -*-
import pytest
from proper_parenthetics import proper_parenthetics


TEST_PROPER_PARENTHETICS_DATA = [
    (')))(((', -1),
    ('()()()()()', 0),
    (')()()()()()', -1),
    ('(((())))', 0),
    ('(()))))))))', -1),
    ('(((((())', 1),
    ('()()()(((', 1)
]


@pytest.mark.parametrize('a_string, result', TEST_PROPER_PARENTHETICS_DATA)
def test_proper_parenthetics(a_string, result):
    """Test proper parenthetics method."""
    assert proper_parenthetics(a_string) == result


def test_proper_parenthetics_empty():
    """Test proper parenthetics method if there are no parenthesis"""
    with pytest.raises(IndexError):
        proper_parenthetics('')
