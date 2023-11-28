from dataclasses import dataclass
from typing import Optional, Any


@dataclass
class QueueElement:
    next: Optional["QueueElement"]
    value: Any


@dataclass
class Queue:
    size: int = 0
    head: Optional[QueueElement] = None
    tail: Optional[QueueElement] = None


def get_new_queue():
    return Queue()


def get_size(queue: Queue):
    return queue.size


def is_empty(queue: Queue):
    return get_size(queue) == 0


def get_head(queue: Queue):
    return None if is_empty(queue) else queue.head.value


def push(queue: Queue, value):
    if is_empty(queue):
        queue.head = QueueElement(None, value)
        queue.tail = queue.head
    else:
        queue.tail.next = QueueElement(None, value)
        queue.tail = queue.tail.next
    queue.size += 1


def pop(queue: Queue):
    if not is_empty(queue):
        queue.head = queue.head.next
        queue.size -= 1
        return True
    return False
