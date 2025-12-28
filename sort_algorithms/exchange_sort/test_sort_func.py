import random

from .sort_func import sort_array


def test_an_empty_array():
    assert sort_array([]) == []


def test_one_element():
    assert sort_array([1]) == [1]


def test_two_elements():
    assert sort_array([1, 2]) == [1, 2]
    assert sort_array([2, 1]) == [1, 2]


def test_three_elements():
    assert sort_array([1, 2, 3]) == [1, 2, 3]
    assert sort_array([2, 1, 3]) == [1, 2, 3]
    assert sort_array([1, 3, 2]) == [1, 2, 3]
    assert sort_array([2, 3, 1]) == [1, 2, 3]
    assert sort_array([3, 1, 2]) == [1, 2, 3]
    assert sort_array([3, 2, 1]) == [1, 2, 3]


def test_four_elements():
    assert sort_array([1, 2, 3, 4]) == [1, 2, 3, 4]
    assert sort_array([1, 2, 4, 3]) == [1, 2, 3, 4]
    assert sort_array([1, 3, 2, 4]) == [1, 2, 3, 4]
    assert sort_array([1, 3, 4, 2]) == [1, 2, 3, 4]
    assert sort_array([2, 1, 3, 4]) == [1, 2, 3, 4]
    assert sort_array([2, 1, 4, 3]) == [1, 2, 3, 4]
    assert sort_array([2, 3, 1, 4]) == [1, 2, 3, 4]
    assert sort_array([2, 3, 4, 1]) == [1, 2, 3, 4]
    assert sort_array([3, 1, 2, 4]) == [1, 2, 3, 4]
    assert sort_array([3, 1, 4, 2]) == [1, 2, 3, 4]
    assert sort_array([3, 2, 1, 4]) == [1, 2, 3, 4]
    assert sort_array([3, 2, 4, 1]) == [1, 2, 3, 4]
    assert sort_array([4, 1, 2, 3]) == [1, 2, 3, 4]
    assert sort_array([4, 1, 3, 2]) == [1, 2, 3, 4]
    assert sort_array([4, 2, 1, 3]) == [1, 2, 3, 4]
    assert sort_array([4, 2, 3, 1]) == [1, 2, 3, 4]
    assert sort_array([4, 3, 1, 2]) == [1, 2, 3, 4]
    assert sort_array([4, 3, 2, 1]) == [1, 2, 3, 4]


def test_random_cases():
    for _ in range(100):
        arr = [random.randint(1, 100) for _ in range(random.randint(5, 100))]
        assert sort_array(arr) == sorted(arr)
