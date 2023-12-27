import pytest
from src.practices.practice9.main import *
from io import StringIO


@pytest.mark.parametrize(
    "string,expected",
    [
        ("aaaaaaaabb", True),
        ("bbabb", True),
        ("ababababb", True),
        ("cabb", False),
        ("ab", False),
        ("", False),
        ("21334242", False),
    ],
)
def test_fsm1_validation(string, expected):
    a = 1
    a += 2
    assert validate_string(create_fsm1(), string) == expected


@pytest.mark.parametrize(
    "string,expected",
    [
        ("8", True),
        ("1.4", True),
        ("21.3E+123423", True),
        ("934E-2", True),
        ("921.", False),
        ("", False),
        ("43.12E", False),
        ("32E+", False),
        ("123.124324E-123131231", True),
        ("abb", False),
    ],
)
def test_fsm2_validation(string, expected):
    assert validate_string(create_fsm2(), string) == expected


@pytest.mark.parametrize(
    "user_input,expected",
    [
        ("ababb", "Your string belongs to first language: (a|b)*abb\n"),
        (
            "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbabb",
            "Your string belongs to first language: (a|b)*abb\n",
        ),
        (
            "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabb",
            "Your string belongs to first language: (a|b)*abb\n",
        ),
        ("abb", "Your string belongs to first language: (a|b)*abb\n"),
        ("baba", "Language was not found\n"),
        ("fact", "Language was not found\n"),
        (
            "10",
            "Your string belongs to second language: digit+(.digit+)?(E(+|-)?digit+)?\n",
        ),
        (
            "10E+2",
            "Your string belongs to second language: digit+(.digit+)?(E(+|-)?digit+)?\n",
        ),
        (
            "43E-13",
            "Your string belongs to second language: digit+(.digit+)?(E(+|-)?digit+)?\n",
        ),
        (
            "324.543363453",
            "Your string belongs to second language: digit+(.digit+)?(E(+|-)?digit+)?\n",
        ),
        (
            "5675.4556765E+12",
            "Your string belongs to second language: digit+(.digit+)?(E(+|-)?digit+)?\n",
        ),
        (
            "10.25E7",
            "Your string belongs to second language: digit+(.digit+)?(E(+|-)?digit+)?\n",
        ),
        (
            "0.71",
            "Your string belongs to second language: digit+(.digit+)?(E(+|-)?digit+)?\n",
        ),
        (
            "777E23",
            "Your string belongs to second language: digit+(.digit+)?(E(+|-)?digit+)?\n",
        ),
        (".12", "Language was not found\n"),
        ("1.5E-", "Language was not found\n"),
        ("1.", "Language was not found\n"),
        ("21.23E+-3", "Language was not found\n"),
        ("12E12+1", "Language was not found\n"),
    ],
)
def test_main(monkeypatch, user_input, expected):
    monkeypatch.setattr("builtins.input", lambda _: user_input)
    fake_output = StringIO()
    monkeypatch.setattr("sys.stdout", fake_output)
    main()
    assert fake_output.getvalue() == expected
