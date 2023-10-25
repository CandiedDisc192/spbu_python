import pytest
from src.practices.practice6.task1 import *
from io import StringIO


@pytest.mark.parametrize(
    "number,expected",
    [
        ("1.25", True),
        ("-1228cringe.cringe12.fg", False),
        ("-5", True),
        ("WHAT???", False),
        ("-1.4324.2", False),
        ("1,23", False),
        ("-12,123.21", False),
        ("170,000,000", False),
    ],
)
def test_is_float_number(number, expected):
    assert is_float_number(number) == expected


@pytest.mark.parametrize(
    "arguments,expected",
    [
        (["1", "2", "3"], True),
        ([], False),
        (["чё"], False),
        (["-1.21", "0.51", "5.5213"], True),
        (["-2.2", "21.232", "213.21", "7.31"], False),
        (["1.2", "1.123.", "23.12"], False),
    ],
)
def test_is_input_valid(arguments, expected):
    assert is_input_valid(arguments) == expected


@pytest.mark.parametrize(
    "a,b,c,expected",
    [
        [-1.0, 0.35, 0.0, (0, 0.35)],
        [5.0, -5.0, 1.25, (0.5,)],
        [22222.0, 55555.0, 33333.0, (-1.0, -1.5)],
    ],
)
def test_solve_quadratic_equation(a, b, c, expected):
    assert solve_quadratic_equation(a, b, c) == expected


def test_solve_quadratic_equation_value_error():
    with pytest.raises(ValueError):
        solve_quadratic_equation(0.0, 1.0, 3.0)


def test_solve_quadratic_equation_arithmetic_error():
    with pytest.raises(ArithmeticError):
        solve_quadratic_equation(5.0, -5.0, 2.25)


@pytest.mark.parametrize(
    "k,b,expected",
    [
        [7995.0, 167895.0, -21.0],
        [51.21, 0, 0],
        [-321.0, -963.0, -3],
        [-15.5, 31, 2],
    ],
)
def test_solve_linear_equation(k, b, expected):
    assert solve_linear_equation(k, b) == expected


def test_solve_linear_equation_value_error():
    with pytest.raises(ValueError):
        solve_linear_equation(0.0, 91.0)


@pytest.mark.parametrize(
    "arg1,arg2,arg3,expected",
    [
        [-1.0, 0.35, 0.0, (0, 0.35)],
        [5.0, -5.0, 1.25, (0.5,)],
        [22222.0, 55555.0, 33333.0, (-1.0, -1.5)],
        [0.0, 7995.0, 167895.0, (-21.0,)],
        [0.0, 51.21, 0, (0,)],
        [0.0, -321.0, -963.0, (-3,)],
        [0.0, -15.5, 31, (2,)],
    ],
)
def test_get_solved_equation(arg1, arg2, arg3, expected):
    assert get_solved_equation(arg1, arg2, arg3) == expected


def test_get_solved_equation_fails():
    with pytest.raises(ArithmeticError):
        get_solved_equation(0, 0, 0)


@pytest.mark.parametrize(
    "user_input,expected",
    [
        ("2 5 3", "Found solutions to the equation: -1.0 -1.5\n"),
        ("0 2 6", "Found solutions to the equation: -3.0\n"),
        ("0 0 0", "Error during calculations: Equation is not linear or quadratic\n"),
        (
            "-5.87 4.4 -5.86",
            "Error during calculations: To find real roots discriminant must be non-negative\n",
        ),
        ("-16.0 4 -0.25", "Found solutions to the equation: 0.125\n"),
        (
            "foimejrngue uiregnrgbnruoruyryu beurgureburbgry",
            'Incorrect input(follow instructions; use "." not ",").\n',
        ),
        ("-12.23.21 22 32", 'Incorrect input(follow instructions; use "." not ",").\n'),
        ("53 21 amogsus", 'Incorrect input(follow instructions; use "." not ",").\n'),
        ("1 1", 'Incorrect input(follow instructions; use "." not ",").\n'),
    ],
)
def test_main(monkeypatch, user_input, expected):
    monkeypatch.setattr("builtins.input", lambda _: user_input)
    fake_output = StringIO()
    monkeypatch.setattr("sys.stdout", fake_output)
    main()
    assert fake_output.getvalue() == expected
