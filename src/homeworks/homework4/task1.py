def add_leading_digits(bin_num: str, digits_count: int) -> str:
    return bin_num[0] * digits_count + bin_num


def delete_leading_digits(bin_num: str) -> str:
    sign_digit = bin_num[0]
    return sign_digit + bin_num.lstrip(sign_digit)


def get_positive_bin(num: int) -> str:
    result = ""
    num = abs(num)
    while num != 0:
        result = str(num % 2) + result
        num //= 2
    return result if result else "0"


def invert_bin(bin_num: str) -> str:
    return "".join(map(lambda x: str(int(x == "0")), bin_num))


def get_opposite_bin(bin_num: str) -> str:
    return get_bin_sum(invert_bin(bin_num), "01")


def get_bin_sum(max_bin: str, min_bin: str) -> str:
    outcomes = ("00", "01", "10", "11")
    min_bin, max_bin = sorted((max_bin, min_bin), key=len)
    min_bin = add_leading_digits(min_bin, len(max_bin) - len(min_bin))
    sum_bin, previous_overflow = "", "0"
    for i in range(len(max_bin) - 1, -1, -1):
        digits_sum = int(previous_overflow) + int(max_bin[i]) + int(min_bin[i])
        previous_overflow = outcomes[digits_sum][0]
        sum_bin += outcomes[digits_sum][1]
    sum_bin = (
        sum_bin[::-1] if max_bin[0] != min_bin[0] else previous_overflow + sum_bin[::-1]
    )
    return delete_leading_digits(sum_bin)


def get_twos_complement(num: int) -> str:
    positive_binary = "0" + get_positive_bin(num)
    if num < 0:
        return get_opposite_bin(positive_binary)
    return positive_binary


def get_decimal_representation(bin_num: str) -> str:
    sign = int(bin_num[0])
    bin_num = bin_num if not sign else get_opposite_bin(bin_num)
    absolute_value = 0
    order = 0
    for digit in bin_num[::-1]:
        absolute_value += int(digit) * (2**order)
        order += 1
    return f"{'-' if sign else '+'}{absolute_value}"


def main() -> None:
    try:
        user_num1 = int(input("Enter first integer: "))
        user_num2 = int(input("Enter second integer: "))
    except ValueError:
        print("Input integer numbers.")
        return

    num1, num2 = get_twos_complement(user_num1), get_twos_complement(user_num2)
    bin_sum = get_bin_sum(num1, num2)
    bin_difference = get_bin_sum(num1, get_opposite_bin(num2))
    print(
        f"Two's complement for 1st number: {num1}\n"
        f"Two's complement for 2nd number: {num2}\n"
        f"Sum (base 2): {bin_sum}\n"
        f"Sum (base 10): {get_decimal_representation(bin_sum)}\n"
        f"Difference (base 2): {bin_difference}\n"
        f"Difference (base 10): {get_decimal_representation(bin_difference)}"
    )


if __name__ == "__main__":
    main()
