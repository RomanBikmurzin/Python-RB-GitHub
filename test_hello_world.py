import pytest


def say_hello():
    greeting_phrase = "hello world"
    return greeting_phrase


@pytest.mark.parametrize(
    "expected_result",
    [
        ("hello world"),  # Можно добавить больше тестовых случаев
        # ("another expected",),  # Пример дополнительного тестового случая
    ],
)
def test_say_hello(expected_result):  # Добавляем параметр в функцию теста
    actual_result = say_hello()
    assert (
        actual_result == expected_result
    ), f"Expected: '{expected_result}', got: '{actual_result}'"
