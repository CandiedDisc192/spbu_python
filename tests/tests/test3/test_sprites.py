import pytest
from src.tests.test3.task1 import *
from io import StringIO


@pytest.mark.parametrize(
    "sprite,expected",
    [
        ([[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]], "   \n   \n   \n"),
        ([[" "]], " \n"),
        ([["█", "█"], ["█", "█"]], "██\n██\n"),
        ([["█", " ", "█"], ["█", " ", "█"], ["█", " ", "█"]], "█ █\n█ █\n█ █\n"),
    ],
)
def test_get_representation(sprite, expected):
    assert get_representation(sprite) == expected


def is_vertical_symmetric(sprite):
    for i in range(len(sprite)):
        for j in range(len(sprite)):
            if sprite[i][j] != sprite[i][-j - 1] or len(sprite) != len(sprite[i]):
                return False
    return True


def is_horizontal_symmetric(sprite):
    for i in range(len(sprite)):
        for j in range(len(sprite)):
            if sprite[i][j] != sprite[-i - 1][j] or len(sprite) != len(sprite[i]):
                return False
    return True


@pytest.mark.parametrize("size", [1, 2, 3, 4, 5, 6, 7, 8, 9])
def test_get_vertical_sprite(size):
    assert is_vertical_symmetric(get_vertical_sprite(size))


@pytest.mark.parametrize("size", [1, 2, 3, 4, 5, 6, 7, 8, 9])
def test_get_horizontal_sprite(size):
    assert is_horizontal_symmetric(get_horizontal_sprite(size))


@pytest.mark.parametrize("size", [1, 2, 3, 4, 5, 6, 7, 8, 9])
def test_get_mixed_sprite(size):
    assert is_horizontal_symmetric(get_mixed_sprite(size)) and is_vertical_symmetric(
        get_mixed_sprite(size)
    )


@pytest.mark.parametrize(
    "user_input,expected",
    [
        (iter(["0"]), "Size must be positive, max size is 1000\n"),
        (iter(["-1"]), "Size must be positive, max size is 1000\n"),
        (iter(["ab"]), "Size must be integer.\n"),
        (iter(["5", "0"]), random_generation(5)),
        (iter(["8", "0"]), random_generation(8)),
    ],
)
def test_main(monkeypatch, user_input, expected):
    monkeypatch.setattr("builtins.input", lambda _: next(user_input))
    fake_output = StringIO()
    monkeypatch.setattr("sys.stdout", fake_output)
    main()
    assert (
        (fake_output.getvalue() == expected)
        or is_vertical_symmetric(expected)
        or is_horizontal_symmetric(expected)
    )
