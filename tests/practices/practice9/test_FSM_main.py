import pytest
from src.practices.practice9.main import *
from io import StringIO


@pytest.mark.parametrize(
    "cur_state,symbol,expected",
    [
        (0, "a", 1),
        (0, "b", 0),
        (1, "a", 1),
        (2, "b", 3),
        (2, "a", 1),
        (3, "b", 0),
        (3, "a", 1),
    ],
)
def test_next_state1(cur_state, symbol, expected):
    assert next_state1(cur_state, symbol) == expected


@pytest.mark.parametrize(
    "cur_state,symbol,expected",
    [
        (0, "1", 1),
        (0, "+", -1),
        (1, "0", 1),
        (1, "E", 4),
        (1, ".", 2),
        (2, "5", 3),
        (2, ".", -1),
        (3, "2", 3),
        (3, "E", 4),
        (3, "-", -1),
        (4, "+", 5),
        (4, "-", 5),
        (4, "7", 6),
        (5, "8", 6),
        (5, "E", -1),
        (6, "8", 6),
        (6, "-", -1),
    ],
)
def test_next_state2(cur_state, symbol, expected):
    assert next_state2(cur_state, symbol) == expected


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
