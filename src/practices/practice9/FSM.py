from dataclasses import dataclass


@dataclass
class FSMachine:
    transition_table: dict[int, dict[str, int]]
    initial_state: int
    final_states: list[int]
    name: str
    pattern: str


def create_fs_machine(
    trans_table: dict[int, dict[str, int]],
    initial_state,
    final_states: list[int],
    fsm_name: str,
    fsm_pattern: str,
) -> FSMachine:
    return FSMachine(trans_table, initial_state, final_states, fsm_name, fsm_pattern)


def validate_string(fsm: FSMachine, string: str) -> bool:
    current_state = fsm.initial_state
    for symbol in string:
        current_state = fsm.transition_table[current_state].get(symbol)
        if current_state is None:
            return False
    return current_state in fsm.final_states
