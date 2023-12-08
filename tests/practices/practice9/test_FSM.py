import pytest
from src.practices.practice9.FSM import create_fs_machine, validate_string


# fsm 1
def next_state_test1(cur_state, symbol):
    state_transitions = {
        (0, "s"): 1,
        (1, "t"): 2,
        (2, "a"): 3,
        (3, "r"): 4,
        (4, "t"): 5,
        (5, "t"): 5,
        (5, "e"): 6,
        (6, "n"): 7,
        (7, "d"): 8,
        (8, "d"): 8,
    }
    try:
        return state_transitions[(cur_state, symbol)]
    except KeyError:
        return "FAIL_STATE"


fsm_test1 = create_fs_machine(
    [0, 1, 2, 3, 4, 5, 6, 7, 8],
    ["s", "t", "a", "r", "e", "n", "d"],
    next_state_test1,
    0,
    [8],
)
CUSTOM_FAIL_STATE = -1


# fsm 2
def next_state_test2(cur_state: int, symbol: str) -> int:
    if cur_state == 0:
        if symbol == "+":
            return 1
        if symbol == "8":
            return 2
        return CUSTOM_FAIL_STATE
    if cur_state == 1:
        if symbol == "7":
            return 2
        return CUSTOM_FAIL_STATE
    if 2 <= cur_state:
        if symbol.isdigit():
            return cur_state + 1
        return CUSTOM_FAIL_STATE


fsm_test2 = create_fs_machine(
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    ["+", *(str(n) for n in range(10))],
    next_state_test2,
    0,
    [12],
)


@pytest.mark.parametrize(
    "fsm,string,expected",
    [
        (fsm_test1, "startend", True),
        (fsm_test1, "startttttendddddddd", True),
        (fsm_test1, "staaartend", False),
        (fsm_test1, "nachalokonec", False),
        (fsm_test2, "+79877545914", True),
        (fsm_test2, "89877545914", True),
        (fsm_test2, "-71221222222", False),
        (fsm_test2, "8123456789", False),
        (fsm_test2, "+712345678901234", False),
        (fsm_test2, "+7 (915) 777 12 34", False),
    ],
)
def test_validate_string(fsm, string, expected):
    assert validate_string(fsm, string, CUSTOM_FAIL_STATE) == expected
