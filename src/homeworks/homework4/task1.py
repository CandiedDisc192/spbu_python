def clean_leading_trash(bin_num: str):
    sign_digit = bin_num[0]
    return sign_digit + bin_num.lstrip(sign_digit)


def get_positive_bin(num: int):
    result = ""
    num = abs(num)
    while num != 0:
        result = str(num % 2) + result
        num //= 2
    return result if result else "0"


def invert_bin(bin_num: str):
    inverted = ""
    for digit in bin_num:
        inverted += "0" if digit == "1" else "1"
    return inverted


def get_opposite_bin(bin_num: str):
    return get_bin_sum(invert_bin(bin_num), "01")


def get_bin_sum(bin1: str, bin2: str):
    outcomes = ("00", "01", "10", "11")
    bin2, bin1 = sorted((bin1, bin2), key=len)
    bin2 = (len(bin1) - len(bin2)) * bin2[0] + bin2
    res, previous_overflow = "", "0"
    for i in range(len(bin1) - 1, -1, -1):
        cur_sum = int(previous_overflow) + int(bin1[i]) + int(bin2[i])
        previous_overflow = outcomes[cur_sum][0]
        res += outcomes[cur_sum][1]
    res = res[::-1] if bin1[0] != bin2[0] else previous_overflow + res[::-1]
    return clean_leading_trash(res)


def get_twos_compliment(num: int):
    sign = num < 0
    casual_bin = "0" + get_positive_bin(num)
    if sign:
        return get_opposite_bin(casual_bin)
    return casual_bin


def get_decimal_representation(bin_num: str):
    sign = int(bin_num[0])
    bin_num = bin_num if not sign else get_opposite_bin(bin_num)
    absolute_value = 0
    degree = 0
    for digit in bin_num[::-1]:
        absolute_value += int(digit) * (2**degree)
        degree += 1
    return int(f"{'-' if sign else ''}{absolute_value}")


def main():
    try:
        user_num1 = int(input("Enter first integer: "))
        user_num2 = int(input("Enter second integer: "))
    except ValueError:
        print("Input integer numbers.")
        return

    processed_num1, processed_num2 = get_twos_compliment(
        user_num1
    ), get_twos_compliment(user_num2)
    bin_sum = get_bin_sum(processed_num1, processed_num2)
    bin_difference = get_bin_sum(processed_num1, get_opposite_bin(processed_num2))
    print(
        f"Two's complement for 1st number: {processed_num1}\n"
        f"Two's complement for 2nd number: {processed_num2}\n"
        f"Sum (base 2): {bin_sum}\n"
        f"Sum (base 10): {get_decimal_representation(bin_sum)}\n"
        f"Difference (base 2): {bin_difference}\n"
        f"Difference (base 10): {get_decimal_representation(bin_difference)}"
    )


if __name__ == "__main__":
    main()
