from dataclasses import dataclass
from typing import Any, Callable


@dataclass
class FSMachine:
    states: list
    inputs: list
    initial_state: Any
    final_states: list
    states_table: dict


def create_fs_machine(states, inputs, initial_state, final_states, table) -> FSMachine:
    return FSMachine(states, inputs, initial_state, final_states, table)


def validate_string(fsm: FSMachine, string: str) -> bool:
    current_state = fsm.initial_state
    for symbol in string:
        if symbol not in fsm.inputs:
            return False
        try:
            current_state = fsm.states_table[(current_state, symbol)]
        except KeyError:
            return False
    return current_state in fsm.final_states
