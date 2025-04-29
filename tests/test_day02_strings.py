"""
Tests for the Day 02 strings drill.
"""

from practice import day02_strings as d2


def test_string_transform_and_vowel_count():
    assert d2.out == "WORLD HELLO!"
    assert d2.vowel_count == 5
