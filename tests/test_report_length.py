from lib.report_length import *

def test_if_string_is_10_chars():
    assert report_length("AVJehoshua") == "This string was 10 characters long."


def test_if_string_is_6_chars():
    assert report_length("Absurd") == "This string was 6 characters long."


def test_if_string_is_5_chars():
    assert report_length("Lawal") == "This string was 5 characters long."


