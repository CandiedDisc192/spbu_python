from FSM import *


def create_fsm1():
    state_table1 = {
        (0, "a"): 1,
        (0, "b"): 0,
        (1, "a"): 1,
        (1, "b"): 2,
        (2, "a"): 1,
        (2, "b"): 3,
        (3, "a"): 1,
        (3, "b"): 0,
    }
    return create_fs_machine([0, 1, 2, 3], ["a", "b"], 0, [3], state_table1)


def main():
    first_fsm = create_fsm1()
    user_string = input("Enter any string: ")
    if validate_string(first_fsm, user_string):
        print("Your string belongs to the first language: (a|b)*abb")
    else:
        print("Language was not found")


if __name__ == "__main__":
    main()
