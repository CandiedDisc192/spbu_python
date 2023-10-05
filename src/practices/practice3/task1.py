def get_dividers(num):
    dividers = []
    possible_divider = 2
    while possible_divider**2 < num:
        if num % possible_divider == 0:
            dividers.append(possible_divider)
            dividers.append(num // possible_divider)
        possible_divider += 1
    if possible_divider**2 == num:
        dividers.append(possible_divider)
    return sorted(dividers)


def is_reducible(num1, num2):
    min_num = min(num1, num2)
    max_num = max(num1, num2)
    if max_num % min_num == 0 and min_num != 1:
        return True
    min_num_dividers = get_dividers(min_num)
    for divider in min_num_dividers:
        if max_num % divider == 0:
            return True
    return False


def get_irreducible_fractions(max_denominator):
    numerators_denominators = []
    for denominator in range(max_denominator, 1, -1):
        for numerator in range(1, denominator):
            if not is_reducible(numerator, denominator):
                numerators_denominators.append((numerator, denominator))
    return sorted(numerators_denominators, key=lambda n_d: n_d[0] / n_d[1])


if __name__ == "__main__":
    n = int(input("Введите число n: "))
    print(
        "Все простые несократимые дроби в порядке возрастания,"
        " заключенные между 0 и 1, знаменатели которых не превышают n:"
    )
    print(*[f"{i}/{j}" for i, j in get_irreducible_fractions(n)], sep=", ")
