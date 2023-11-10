import pytest
from src.homeworks.homework5.task1 import *
from io import StringIO


@pytest.mark.parametrize(
    "symbol_ord,expected",
    [(1, "U+0001"), (1048576, "U+100000"), (1114109, "U+10FFFD"), (11088, "U+2B50")],
)
def test_get_unicode_num(symbol_ord, expected):
    assert get_unicode_num(symbol_ord) == expected


@pytest.mark.parametrize(
    "string,part_len,sep,expected",
    [
        ("abc", 1, "|", "a|b|c"),
        ("0001000010000000", 8, " ", "00010000 10000000"),
        (
            "11111111111111111111111111111111",
            8,
            " ",
            "11111111 11111111 11111111 11111111",
        ),
        ("all all all all all all", 23, "AAAA", "all all all all all all"),
        ("123456789", 3, ".aaaa.", "123.aaaa.456.aaaa.789"),
    ],
)
def test_divide_equally(string, part_len, sep, expected):
    assert divide_equally(string, part_len, sep) == expected


@pytest.mark.parametrize(
    "symbol_ord,expected",
    [
        (194619, "11011000 01111110 11011100 00111011"),
        (49, "00000000 00110001"),
        (27701, "01101100 00110101"),
        (33, "00000000 00100001"),
    ],
)
def test_get_bin_representation(symbol_ord, expected):
    assert get_bin_representation(symbol_ord) == expected


@pytest.mark.parametrize(
    "user_input,expected",
    [
        (
            "Hello, World!",
            "UTF-16 encoding:\n"
            "H\tU+0048\t00000000 01001000\n"
            "e\tU+0065\t00000000 01100101\n"
            "l\tU+006C\t00000000 01101100\n"
            "l\tU+006C\t00000000 01101100\n"
            "o\tU+006F\t00000000 01101111\n"
            ",\tU+002C\t00000000 00101100\n"
            " \tU+0020\t00000000 00100000\n"
            "W\tU+0057\t00000000 01010111\n"
            "o\tU+006F\t00000000 01101111\n"
            "r\tU+0072\t00000000 01110010\n"
            "l\tU+006C\t00000000 01101100\n"
            "d\tU+0064\t00000000 01100100\n"
            "!\tU+0021\t00000000 00100001\n",
        ),
        ("絣", "UTF-16 encoding:\n" "絣\tU+2F96C\t11011000 01111110 11011101 01101100\n"),
        (
            "⛽✈𭎗𢦜ꓨ",
            "UTF-16 encoding:\n"
            "⛽\tU+26FD\t00100110 11111101\n"
            "✈\tU+2708\t00100111 00001000\n"
            "𭎗\tU+2D397\t11011000 01110100 11011111 10010111\n"
            "𢦜\tU+2299C\t11011000 01001010 11011101 10011100\n"
            "ꓨ\tU+A4E8\t10100100 11101000\n",
        ),
        (
            "ඞ amogus",
            "UTF-16 encoding:\n"
            "ඞ\tU+0D9E\t00001101 10011110\n"
            " \tU+0020\t00000000 00100000\n"
            "a\tU+0061\t00000000 01100001\n"
            "m\tU+006D\t00000000 01101101\n"
            "o\tU+006F\t00000000 01101111\n"
            "g\tU+0067\t00000000 01100111\n"
            "u\tU+0075\t00000000 01110101\n"
            "s\tU+0073\t00000000 01110011\n",
        ),
    ],
)
def test_main(monkeypatch, user_input, expected):
    monkeypatch.setattr("builtins.input", lambda _: user_input)
    fake_output = StringIO()
    monkeypatch.setattr("sys.stdout", fake_output)
    main()
    assert fake_output.getvalue() == expected
