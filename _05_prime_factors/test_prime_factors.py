from .prime_factors import generate_prime_factors


def test_number_1_returns_empty_list():
    assert generate_prime_factors(1) == []


def test_number_2_and_3_returns_list_with_single_element():
    assert generate_prime_factors(2) == [2]
    assert generate_prime_factors(3) == [3]
    assert generate_prime_factors(5) == [5]
    assert generate_prime_factors(7) == [7]


def test_numbers_has_less_than_four_factors():
    assert generate_prime_factors(4) == [2, 2]
    assert generate_prime_factors(6) == [2, 3]
    assert generate_prime_factors(8) == [2, 2, 2]
    assert generate_prime_factors(9) == [3, 3]
