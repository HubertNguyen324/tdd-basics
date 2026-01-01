from .roman_num import convert_to_roman


def test_from_1_to_10():
    assert convert_to_roman(1) == "I"
    assert convert_to_roman(2) == "II"
    assert convert_to_roman(3) == "III"
    assert convert_to_roman(4) == "IV"
    assert convert_to_roman(5) == "V"
    assert convert_to_roman(6) == "VI"
    assert convert_to_roman(7) == "VII"
    assert convert_to_roman(8) == "VIII"
    assert convert_to_roman(9) == "IX"
    assert convert_to_roman(10) == "X"


def test_from_11_to_20():
    assert convert_to_roman(11) == "XI"
    assert convert_to_roman(12) == "XII"
    assert convert_to_roman(13) == "XIII"
    assert convert_to_roman(14) == "XIV"
    assert convert_to_roman(15) == "XV"
    assert convert_to_roman(16) == "XVI"
    assert convert_to_roman(17) == "XVII"
    assert convert_to_roman(18) == "XVIII"
    assert convert_to_roman(19) == "XIX"
    assert convert_to_roman(20) == "XX"


def test_from_99_to_111():
    assert convert_to_roman(99) == "XCIX"
    assert convert_to_roman(100) == "C"
    assert convert_to_roman(101) == "CI"
    assert convert_to_roman(102) == "CII"
    assert convert_to_roman(103) == "CIII"
    assert convert_to_roman(104) == "CIV"
    assert convert_to_roman(105) == "CV"
    assert convert_to_roman(106) == "CVI"
    assert convert_to_roman(107) == "CVII"
    assert convert_to_roman(108) == "CVIII"
    assert convert_to_roman(109) == "CIX"
    assert convert_to_roman(110) == "CX"
    assert convert_to_roman(111) == "CXI"


def test_from_999_to_1111():
    assert convert_to_roman(999) == "CMXCIX"
    assert convert_to_roman(1000) == "M"
    assert convert_to_roman(1001) == "MI"
    assert convert_to_roman(1002) == "MII"
    assert convert_to_roman(1003) == "MIII"
    assert convert_to_roman(1004) == "MIV"
    assert convert_to_roman(1005) == "MV"
    assert convert_to_roman(1006) == "MVI"
    assert convert_to_roman(1007) == "MVII"
    assert convert_to_roman(1008) == "MVIII"
    assert convert_to_roman(1009) == "MIX"
    assert convert_to_roman(1010) == "MX"
    assert convert_to_roman(1011) == "MXI"
