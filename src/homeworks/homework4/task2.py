def get_float_bin(num: float):
    int_part_bin = bin(abs(int(num)))[2:]
    fractional_part_bin = ""
    fractional_part = num - int(num)
    while fractional_part != int(fractional_part):
        fractional_part *= 2
        fractional_part_bin += str(int(fractional_part) % 2)
    return f"{'-' if num < 0 else '+'}{int_part_bin}.{fractional_part_bin if fractional_part else '0'}"


def normalize(num: float):
    float_bin = get_float_bin(num)
    unsigned_bin = float_bin[1:]
    num_sign = float_bin[0]
    mantissa = unsigned_bin.replace(".", "").lstrip("0") if num != 0 else "0"
    order = (
        unsigned_bin.find(".")
        if unsigned_bin[0] != "0"
        else -len(unsigned_bin[2 : unsigned_bin.find(mantissa[0])])
    )
    return f"{num_sign}0.{mantissa}*2^{order}"


def to_fp(normalized: str, bits: int):
    bits_to_exponent = {64: 11, 32: 8, 16: 5}
    mantissa_bits = bits - bits_to_exponent[bits] - 1
    exp_i = normalized.find("^")
    sign, mantissa, original_order = (
        int(normalized[0] == "-"),
        normalized[3 : exp_i - 2],
        int(normalized[exp_i + 1 :]),
    )
    shifted_order = bin(original_order + (2 ** (bits_to_exponent[bits] - 1)) - 1)[2:]
    mantissa += (mantissa_bits - len(mantissa)) * "0"
    shifted_order += (bits_to_exponent[bits] - len(shifted_order)) * "0"
    return f"{sign}{shifted_order}{mantissa[:mantissa_bits]}"


def main():
    user_num = input("Enter a number: ")
    try:
        user_num = float(user_num)
    except ValueError:
        print("Enter float or integer number.")
        return
    normalized_input = normalize(user_num)
    print(f"Result: {normalized_input }")
    user_choose = input(
        "Available formats:\n1. FP64\n2. FP32\n3. FP16\nEnter selection(1-3): "
    )
    if user_choose == "1":
        print(to_fp(normalized_input, 64))
    elif user_choose == "2":
        print(to_fp(normalized_input, 32))
    elif user_choose == "3":
        print(to_fp(normalized_input, 16))
    else:
        print("Undefined option.")


if __name__ == "__main__":
    main()
