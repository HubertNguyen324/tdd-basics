from .leap_year import is_leap_year


def test_year_divide_by_4():
    assert is_leap_year(2020)
    assert not is_leap_year(2019)
    assert not is_leap_year(2018)
    assert not is_leap_year(2017)
    assert is_leap_year(2016)


def test_year_is_divisible_by_100():
    assert not is_leap_year(1900)
    assert not is_leap_year(2200)
    assert not is_leap_year(2300)
    assert is_leap_year(2400)
    assert not is_leap_year(1100)


def test_year_is_divisible_by_400():
    assert is_leap_year(2000)
    assert is_leap_year(2400)
    assert not is_leap_year(1800)
    assert not is_leap_year(1900)
    assert not is_leap_year(2100)
    assert not is_leap_year(2200)
    assert not is_leap_year(2300)
