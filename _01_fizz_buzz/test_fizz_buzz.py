from .fizz_buzz import fizz_buzz


def test_not_multiple_of_3_or_5():
    assert fizz_buzz(1) == "1"
    assert fizz_buzz(2) == "2"
    assert fizz_buzz(4) == "4"
    assert fizz_buzz(7) == "7"
    assert fizz_buzz(8) == "8"


def test_multiple_of_only_3():
    assert fizz_buzz(3) == "Fizz"
    assert fizz_buzz(6) == "Fizz"
    assert fizz_buzz(9) == "Fizz"
    assert fizz_buzz(12) == "Fizz"
    assert fizz_buzz(18) == "Fizz"


def test_multiple_of_only_5():
    assert fizz_buzz(5) == "Buzz"
    assert fizz_buzz(10) == "Buzz"
    assert fizz_buzz(20) == "Buzz"
    assert fizz_buzz(25) == "Buzz"
    assert fizz_buzz(35) == "Buzz"


def test_multiple_of_3_and_5():
    assert fizz_buzz(15) == "FizzBuzz"
    assert fizz_buzz(30) == "FizzBuzz"
    assert fizz_buzz(45) == "FizzBuzz"
    assert fizz_buzz(60) == "FizzBuzz"
    assert fizz_buzz(75) == "FizzBuzz"
