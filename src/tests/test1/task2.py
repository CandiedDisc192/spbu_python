from dataclasses import dataclass
from typing import Any, Optional


@dataclass
class DequeElement:
    previous: Optional["DequeElement"]
    next: Optional["DequeElement"]
    value: Any


@dataclass
class Deque:
    first: Optional[DequeElement]
    last: Optional[DequeElement]
    size: int


def create_deque() -> Deque:
    return Deque(None, None, 0)


def size(deq: Deque) -> int:
    return deq.size


def is_empty(deq: Deque) -> bool:
    return size(deq) == 0


def pop_front(deq: Deque) -> Any:
    if is_empty(deq):
        raise ValueError("pop_front from empty deque")
    prev_first = deq.first.value
    deq.first = deq.first.next
    deq.size -= 1

    if deq.size == 1:
        deq.first = deq.last
    elif is_empty(deq):
        deq.last = None
    return prev_first


def push_front(deq: Deque, value: Any):
    if is_empty(deq):
        deq.first = DequeElement(None, None, value)
        deq.last = deq.first
        deq.size += 1
        return
    deq.first.previous = DequeElement(None, deq.first, value)
    deq.first = deq.first.previous
    deq.size += 1


def pop_back(deq: Deque) -> Any:
    if is_empty(deq):
        raise ValueError("pop_back from empty deque")
    prev_last = deq.last.value
    deq.last = deq.last.previous
    deq.size -= 1
    if deq.size == 1:
        deq.last = deq.first
    elif is_empty(deq):
        deq.first = None

    return prev_last


def push_back(deq: Deque, value: Any):
    if is_empty(deq):
        deq.first = DequeElement(None, None, value)
        deq.last = deq.first
        deq.size += 1
        return
    deq.last.next = DequeElement(deq.last, None, value)
    deq.last = deq.last.next
    deq.size += 1
