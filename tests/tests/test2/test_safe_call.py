import pytest
from src.tests.test2.task2r import *


@safe_call
def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("Dividing by zero.")
    return x / y


@pytest.mark.parametrize(
    "x,y,expected",
    [
        (6, 3, 2.0),
        (101, 50.5, 2.0),
        ({1, 2, 3}, [12321], None),
        (7, 0, None),
        (9, "as", None),
        ("", "", None),
        (None, 10, None),
    ],
)
def test_safe_divide(x, y, expected):
    with warnings.catch_warnings(record=True) as warnings_list:
        if expected is not None:
            assert divide(x, y) == expected and len(warnings_list) == 0
        else:
            assert divide(x, y) == expected and len(warnings_list) == 1


@pytest.mark.parametrize(
    "x,y,expected",
    [
        (
            1,
            0,
            f"\nError in function divide.\nFile {__file__}\nType: ZeroDivisionError\nMessage: Dividing by zero.\n"
            f'On line 8: raise ZeroDivisionError("Dividing by zero.")',
        ),
        (
            "as",
            "As",
            f"\nError in function divide.\nFile {__file__}\nType: TypeError\nMessage: unsupported operand type(s) for /:"
            f" 'str' and 'str'\nOn line 9: return x / y",
        ),
        (
            7,
            "As",
            f"\nError in function divide.\nFile {__file__}\nType: TypeError\nMessage: unsupported operand type(s) for /:"
            f" 'int' and 'str'\nOn line 9: return x / y",
        ),
        (
            [1],
            21,
            f"\nError in function divide.\nFile {__file__}\nType: TypeError\nMessage: unsupported operand type(s) for /:"
            f" 'list' and 'int'\nOn line 9: return x / y",
        ),
    ],
)
def test_safe_divide_warning(x, y, expected):
    with warnings.catch_warnings(record=True) as warnings_list:
        divide(x, y)
        assert str(warnings_list[0].message) == expected


@safe_call
def inverse(bin_n):
    res = ""
    for n in bin_n:
        if n != "0" and n != "1":
            raise ValueError("Arg is not binary")
        res += str(int(not int(n)))
    return res


@pytest.mark.parametrize(
    "bin_n,expected",
    [
        ("101", "010"),
        ("10101010101", "01010101010"),
        ("172", None),
        ("erregre", None),
        (10101, None),
        (["1010101"], None),
    ],
)
def test_safe_inverse(bin_n, expected):
    with warnings.catch_warnings(record=True) as warnings_list:
        if expected is not None:
            assert inverse(bin_n) == expected and len(warnings_list) == 0
        else:
            assert inverse(bin_n) == expected and len(warnings_list) == 1


@pytest.mark.parametrize(
    "bin_n,expected",
    [
        (
            "9999",
            f"\nError in function inverse.\nFile {__file__}\nType: ValueError\nMessage: Arg is not binary\n"
            f'On line 57: raise ValueError("Arg is not binary")',
        )
    ],
)
def test_safe_inverse_warning(bin_n, expected):
    with warnings.catch_warnings(record=True) as warnings_list:
        inverse(bin_n)
        assert str(warnings_list[0].message) == expected
