import pytest


def say_hello():
    greeting_phrase = "hello world"
    return greeting_phrase


def test_say_hello():
    actual_result = say_hello()
    assert actual_result == expected_result
