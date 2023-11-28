from task2 import *


my_deq1 = create_deque()
print("DEQUE 1:")
for i in range(1, 6):
    push_front(my_deq1, i)
    push_back(my_deq1, -i)
for j in range(1, 11):
    print(f"{j}. current size: {size(my_deq1)}")
    print(f"delete value: {pop_front(my_deq1)}")

my_deq2 = create_deque()
print("\nDEQUE 2:")
for i in range(1, 6):
    push_front(my_deq2, i)
    push_back(my_deq2, -i)
for j in range(1, 11):
    print(f"{j}. current size: {size(my_deq2)}")
    print(f"delete value: {pop_back(my_deq2)}")


my_deq3 = create_deque()
print("\nDEQUE 3:")
push_front(my_deq3, None)
push_back(my_deq3, "ABC")
print(pop_front(my_deq3))
print(pop_front(my_deq3))

my_deq4 = create_deque()
print("\nDEQUE 4:")
push_back(my_deq4, 100)
push_front(my_deq4, 25)
for j in range(3):
    try:
        a = pop_back(my_deq4)
    except ValueError as error:
        print(error)
    else:
        print(a)
print(is_empty(my_deq4))
push_back(my_deq4, "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
print(is_empty(my_deq4))

for j in range(2):
    try:
        b = pop_front(my_deq4)
    except ValueError as error:
        print(error)
print(is_empty(my_deq4))


my_deq5 = create_deque()
print("\nDEQUE 5:")
for i in range(1, 6):
    push_front(my_deq5, i)
    push_back(my_deq5, -i)
for j in range(1, 6):
    print(pop_back(my_deq5), pop_front(my_deq5))
print(is_empty(my_deq5))
