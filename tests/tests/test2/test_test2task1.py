import pytest
from src.tests.test2.task1 import *
from io import StringIO


@pytest.mark.parametrize(
    "n,expected",
    [(0, 0), (1, 1), (2, 1), (3, 2), (10, 55), (22, 17711), (90, 2880067194370816120)],
)
def test_fib(n, expected):
    assert fib(n) == expected


def test_fib_value_error():
    with pytest.raises(ValueError):
        fib(-1)
    with pytest.raises(ValueError):
        fib(91)


@pytest.mark.parametrize(
    "user_input,expected",
    [
        ("10", "n-th fibonacci number is 55\n"),
        ("-10", "Argument must be in the range from 0 to 90.\n"),
        ("901", "Argument must be in the range from 0 to 90.\n"),
        ("no", "The entered value is not an integer.\n"),
        ("10.2", "The entered value is not an integer.\n"),
        ("77", "n-th fibonacci number is 5527939700884757\n"),
    ],
)
def test_main(monkeypatch, user_input, expected):
    monkeypatch.setattr("builtins.input", lambda _: user_input)
    fake_output = StringIO()
    monkeypatch.setattr("sys.stdout", fake_output)
    main()
    assert fake_output.getvalue() == expected
