from task3 import *


if __name__ == "__main__":
    my_queue1 = get_new_queue()
    my_queue2 = get_new_queue()
    my_queue3 = get_new_queue()

    print("MY_QUEUE1:")
    print(get_size(my_queue1), get_head(my_queue1))
    push(my_queue1, "Vasya")
    print(get_size(my_queue1), get_head(my_queue1))
    push(my_queue1, "Anya")
    print(get_size(my_queue1), get_head(my_queue1))
    pop(my_queue1)
    print(get_size(my_queue1), get_head(my_queue1))
    pop(my_queue1)
    print(get_size(my_queue1), get_head(my_queue1), is_empty(my_queue1))

    print("MY_QUEUE2:")
    push(my_queue2, 22)
    push(my_queue2, None)
    push(my_queue2, "ABC")
    for _ in range(3):
        print(f"Bye, {get_head(my_queue2)}!")
        pop(my_queue2)

    print("MY_QUEUE3:")
    pop(my_queue3)
    pop(my_queue3)
    pop(my_queue3)
    pop(my_queue3)
    print(get_head(my_queue3))
    push(my_queue3, 888)
    print(get_head(my_queue3))
    pop(my_queue3)
    print(get_head(my_queue3))
