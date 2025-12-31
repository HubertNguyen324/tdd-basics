import random

from .str_calculator import add


def test_add_empty_string_returns_zero():
    assert add("") == 0


def test_add_single_number_returns_number():
    assert add("0") == 0
    assert add("5") == 5
    assert add("10") == 10
    assert add("15") == 15


def test_add_two_numbers_returns_sum():
    assert add("1,2") == 3
    assert add("3,4") == 7
    assert add("5,6") == 11


def test_add_three_numbers_returns_sum():
    assert add("1,2,3") == 6
    assert add("4,5,6") == 15
    assert add("7,8,9") == 24


def test_add_random_numbers_returns_sum():
    for _ in range(100):
        numbers = [random.randint(-100, 100) for _ in range(random.randint(1, 500))]
        input_str = ",".join(map(str, numbers))
        expected_sum = sum(numbers)
        assert add(input_str) == expected_sum


def test_new_line_delimiter():
    assert add("1\n2") == 3
    assert add("3\n4") == 7
    assert add("5\n6") == 11


def test_space_delimiter():
    assert add("1 2") == 3
    assert add("3 4") == 7
    assert add("5 6") == 11
