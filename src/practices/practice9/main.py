from src.practices.practice9.FSM import *


def next_state1(cur_state: int, symbol: str) -> int:
    states_map = {
        (0, "a"): 1,
        (0, "b"): 0,
        (1, "a"): 1,
        (1, "b"): 2,
        (2, "a"): 1,
        (2, "b"): 3,
        (3, "a"): 1,
        (3, "b"): 0,
    }
    return states_map[(cur_state, symbol)]


def next_state2(cur_state: int, symbol: str) -> int:
    # lists indexes correspond to states
    compare_with = [[], [".", "E"], [], ["E"], ["+", "-"], [], []]
    paths_from_states = [[1], [1, 2, 4], [3], [3, 4], [6, 5, 5], [6], [6]]
    state_paths = paths_from_states[cur_state]
    state_checks = compare_with[cur_state]
    if symbol.isdigit():
        return state_paths[0]
    for i in range(len(state_checks)):
        if symbol == state_checks[i]:
            return state_paths[i + 1]
    return -1


def main():
    first_fsm = create_fs_machine([0, 1, 2, 3], ["a", "b"], next_state1, 0, [3])
    second_fsm = create_fs_machine(
        [0, 1, 2, 3, 4, 5, 6],
        [*(str(n) for n in range(10)), ".", "E", "+", "-"],
        next_state2,
        0,
        [1, 3, 6],
    )
    user_string = input("Enter any string: ")
    if validate_string(first_fsm, user_string):
        print("Your string belongs to first language: (a|b)*abb")
    elif validate_string(second_fsm, user_string, -1):
        print(
            "Your string belongs to second language: digit+(.digit+)?(E(+|-)?digit+)?"
        )
    else:
        print("Language was not found")


if __name__ == "__main__":
    main()
