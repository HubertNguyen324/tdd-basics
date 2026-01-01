from .roman_num import convert_to_int


def test_from_1_to_10():
    assert convert_to_int("I") == 1
    assert convert_to_int("II") == 2
    assert convert_to_int("III") == 3
    assert convert_to_int("IV") == 4
    assert convert_to_int("V") == 5
    assert convert_to_int("VI") == 6
    assert convert_to_int("VII") == 7
    assert convert_to_int("VIII") == 8
    assert convert_to_int("IX") == 9
    assert convert_to_int("X") == 10


def test_from_11_to_20():
    assert convert_to_int("XI") == 11
    assert convert_to_int("XII") == 12
    assert convert_to_int("XIII") == 13
    assert convert_to_int("XIV") == 14
    assert convert_to_int("XV") == 15
    assert convert_to_int("XVI") == 16
    assert convert_to_int("XVII") == 17
    assert convert_to_int("XVIII") == 18
    assert convert_to_int("XIX") == 19
    assert convert_to_int("XX") == 20


def test_from_99_to_111():
    assert convert_to_int("XCIX") == 99
    assert convert_to_int("C") == 100
    assert convert_to_int("CI") == 101
    assert convert_to_int("CII") == 102
    assert convert_to_int("CIII") == 103
    assert convert_to_int("CIV") == 104
    assert convert_to_int("CV") == 105
    assert convert_to_int("CVI") == 106
    assert convert_to_int("CVII") == 107
    assert convert_to_int("CVIII") == 108
    assert convert_to_int("CIX") == 109
    assert convert_to_int("CX") == 110
    assert convert_to_int("CXI") == 111


def test_from_111_to_120():
    assert convert_to_int("CXII") == 112
    assert convert_to_int("CXIII") == 113
    assert convert_to_int("CXIV") == 114
    assert convert_to_int("CXV") == 115
    assert convert_to_int("CXVI") == 116
    assert convert_to_int("CXVII") == 117
    assert convert_to_int("CXVIII") == 118
    assert convert_to_int("CXIX") == 119
    assert convert_to_int("CXX") == 120
