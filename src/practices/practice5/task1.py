from dataclasses import dataclass
from collections import namedtuple

StackElement = namedtuple("StackElement", ["next", "value"])


@dataclass
class Stack:
    size: int
    head: StackElement


def get_new_stack():
    return Stack(0, None)


def empty(stack: Stack):
    return stack.size == 0


def size(stack: Stack):
    return stack.size


def top(stack: Stack):
    return None if empty(stack) else stack.head.value


def push(stack: Stack, value):
    element = StackElement(stack.head, value)
    stack.head = element
    stack.size += 1


def pop(stack: Stack):
    if not empty(stack):
        stack.head = stack.head.next
        stack.size -= 1
        return True
    return False


def main():
    my_stack = get_new_stack()
    element1 = 10
    element2 = None
    element3 = "Крутой"

    print(top(my_stack))
    print(empty(my_stack))

    push(my_stack, element1)
    print(top(my_stack))
    print(empty(my_stack))

    push(my_stack, element2)
    print(top(my_stack))
    print(size(my_stack))

    push(my_stack, element3)
    print(top(my_stack))

    pop(my_stack)
    print(top(my_stack))
    print(size(my_stack))


main()
