import pytest
from src.practices.practice9.FSM import create_fs_machine, validate_string


@pytest.fixture
def create_mock_fsm1():
    return create_fs_machine(
        {0: {"0": 1, "1": 1}, 1: {"+": 2, "-": 2}, 2: {"0": 3, "1": 3}, 3: {}},
        0,
        [1, 3],
        "",
        "",
    )


@pytest.mark.parametrize(
    "string,expected",
    [
        ("1+", False),
        ("0-1", True),
        ("1+1", True),
        ("1", True),
        ("L", False),
        ("1+1+1", False),
        ("             1+1", False),
    ],
)
def test_mock_fsm1(string, expected, create_mock_fsm1):
    assert validate_string(create_mock_fsm1, string) == expected


@pytest.fixture
def create_mock_fsm2():
    return create_fs_machine(
        {0: {"e": 1}, 1: {"n": 2}, 2: {"d": 3}, 3: {"!": 0}}, 0, [0], "", ""
    )


@pytest.mark.parametrize(
    "string,expected",
    [
        ("end!", True),
        ("end!end!end!", True),
        ("end", False),
        ("!", False),
        ("osdfdosfkokfeoifkreoige", False),
        ("end!!end!", False),
        ("end?", False),
    ],
)
def test_mock_fsm2(string, expected, create_mock_fsm2):
    assert validate_string(create_mock_fsm2, string) == expected
