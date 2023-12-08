from FSM import *


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


def main():
    first_fsm = create_fs_machine([0, 1, 2, 3], ["a", "b"], next_state1, 0, [3])
    user_string = input("Enter any string: ")
    if validate_string(first_fsm, user_string):
        print("Your string belongs to first language: (a|b)*abb")
    else:
        print("Language was not found")


if __name__ == "__main__":
    main()
