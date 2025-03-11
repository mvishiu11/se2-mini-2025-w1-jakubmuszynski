import pytest   # noqa F401
from calc import calc


def test_empty_string():
    # Given an empty string input
    input_string = ""
    # When the calculator processes the input
    result = calc(input_string)
    # Then the result should be 0
    assert result == 0


def test_single_number():
    # Given
    input_string = "5"
    # When
    result = calc(input_string)
    # Then
    assert result == 5

    # Given
    input_string = "42"
    # When
    result = calc(input_string)
    # Then
    assert result == 42


def test_sum_two():
    # Given
    input_string = "1,2"
    # When
    result = calc(input_string)
    # Then
    assert result == 3

    # Given
    input_string = "1\n2"
    # When
    result = calc(input_string)
    # Then
    assert result == 3


def test_sum_three():
    # Given
    input_string = "1,2\n3"
    # When
    result = calc(input_string)
    # Then
    assert result == 6

    # Given
    input_string = "1\n2,3"
    # When
    result = calc(input_string)
    # Then
    assert result == 6


def test_negatives_not_allowed():
    # Given
    input_string = "1,-2\n3"
    # Then
    with pytest.raises(ValueError):
        # When
        calc(input_string)

    # Given
    input_string = "-1\n-2,-3"
    # Then
    with pytest.raises(ValueError):
        # When
        calc(input_string)

    # Given
    input_string = "-3"
    # Then
    with pytest.raises(ValueError):
        # When
        calc(input_string)


def test_ignore_numbers_greater_than_1000():
    # Given
    input_string = "1001,2\n3"
    # When
    result = calc(input_string)
    # Then
    assert result == 5

    # Given
    input_string = "1000,1001,2\n3"
    # When
    result = calc(input_string)
    # Then
    assert result == 1005


def test_custom_delimiter():
    # Given
    input_string = "//;1;2"
    # When
    result = calc(input_string)
    # Then
    assert result == 3

    # Given
    input_string = "//*3*4,5\n6"
    # When
    result = calc(input_string)
    # Then
    assert result == 18


def test_multiline_delimiter():
    # Given
    input_string = "//[###]\n1###2,3"
    # When
    result = calc(input_string)
    # Then
    assert result == 6

    # Given
    input_string = "//[*][%%]\n1*2%%3,4"
    # When
    result = calc(input_string)
    # Then
    assert result == 10
