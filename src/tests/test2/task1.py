def fib(n: int) -> int:
    if n < 0 or 90 < n:
        raise ValueError("Argument must be in the range from 0 to 90.")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        prev_prev_fib = 0
        prev_fib = 1
        for _ in range(2, n + 1):
            current_fib = prev_prev_fib + prev_fib
            prev_prev_fib = prev_fib
            prev_fib = current_fib
        return prev_fib


def main():
    user_num = input("Enter n: ")
    try:
        user_num = int(user_num)
    except ValueError:
        print("The entered value is not an integer.")
        return
    try:
        n_fib = fib(user_num)
    except ValueError as error:
        print(error)
        return
    print(f"n-th fibonacci number is {n_fib}")


if __name__ == "__main__":
    main()
