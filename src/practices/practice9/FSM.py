from dataclasses import dataclass
from typing import Any, Callable


@dataclass
class FSMachine:
    states: list
    inputs: list
    transition_func: Callable
    initial_state: Any
    final_states: list


def create_fs_machine(
    states: list, inputs: list, trans_func: Callable, initial_state, final_states: list
) -> FSMachine:
    return FSMachine(states, inputs, trans_func, initial_state, final_states)


def validate_string(fsm: FSMachine, string: str, fail_state="FAIL_STATE") -> bool:
    current_state = fsm.initial_state
    for symbol in string:
        if symbol not in fsm.inputs:
            return False
        current_state = fsm.transition_func(current_state, symbol)
        if current_state == fail_state:
            return False
    return current_state in fsm.final_states
