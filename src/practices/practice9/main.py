from src.practices.practice9.FSM import *


def create_fsm1() -> FSMachine:
    trans_rule = {
        0: {"a": 1, "b": 0},
        1: {"a": 1, "b": 2},
        2: {"a": 1, "b": 3},
        3: {"a": 1, "b": 0},
    }
    start_state = 0
    end_states = [3]
    return create_fs_machine(trans_rule, start_state, end_states, "first", "(a|b)*abb")


def create_fsm2() -> FSMachine:
    def digits_to(next_state: int) -> dict[str, int]:
        return {str(i): next_state for i in range(10)}

    trans_rule = {
        0: digits_to(1),
        1: {**digits_to(1), ".": 2, "E": 4},
        2: digits_to(3),
        3: {**digits_to(3), "E": 4},
        4: {**digits_to(6), "+": 5, "-": 5},
        5: digits_to(6),
        6: digits_to(6),
    }
    start_state = 0
    end_states = [1, 3, 6]
    return create_fs_machine(
        trans_rule,
        start_state,
        end_states,
        "second",
        "digit+(.digit+)?(E(+|-)?digit+)?",
    )


def recognize_language(input_string: str, fsm_lst: list[FSMachine]) -> str:
    for fsm in fsm_lst:
        if validate_string(fsm, input_string):
            return f"Your string belongs to {fsm.name} language: {fsm.pattern}"
    return "Language was not found"


def main() -> None:
    fsm1 = create_fsm1()
    fsm2 = create_fsm2()
    fsm_list = [fsm1, fsm2]
    user_string = input("Enter any string: ")
    print(recognize_language(user_string, fsm_list))


if __name__ == "__main__":
    main()
