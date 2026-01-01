ROMAN_NUMERALS = {
    1000: "M",
    900: "CM",
    500: "D",
    400: "CD",
    100: "C",
    90: "XC",
    50: "L",
    40: "XL",
    10: "X",
    9: "IX",
    5: "V",
    4: "IV",
    1: "I",
}


def convert_to_roman(number: int) -> str:
    roman = ""
    for value, numeral in ROMAN_NUMERALS.items():
        while number >= value:
            roman += numeral
            number -= value
    return roman


def convert_to_int(roman: str) -> int:
    result = 0
    for value, numeral in ROMAN_NUMERALS.items():
        while roman.startswith(numeral):
            result += value
            roman = roman[len(numeral) :]
    return result
