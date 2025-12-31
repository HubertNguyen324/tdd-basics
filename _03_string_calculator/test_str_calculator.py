from .str_calculator import add


def test_add_empty_string_returns_zero():
    assert add("") == 0
