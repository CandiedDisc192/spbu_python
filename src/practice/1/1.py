def incomplete_quotient(dividend, divider):
    capacity = 0
    result = 0
    sign = dividend * divider > 0

    dividend = abs(dividend)
    divider = abs(divider)

    while capacity + divider <= dividend:
        capacity += divider
        result += 1
    return result if sign else -result


if __name__ == "__main__":
    try:
        a = int(input("Введите делимое: "))
        b = int(input("Введите делитель: "))
        iq = incomplete_quotient(a, b)
        print("Неполное частное: {}".format(iq))
    except ValueError:
        print("Надо было ввести число")
