def is_prime(num):
    border = num ** 0.5
    possible_divider = 2
    while possible_divider <= border:
        if num % possible_divider == 0:
            return False
        possible_divider += 1
    return True


if __name__ == "__main__":
    a = int(input("Введите число: "))
    print("Все простые чилса, не превосходящие {}:".format(a))
    for n in range(2, a):
        if is_prime(n):
            print(n)
