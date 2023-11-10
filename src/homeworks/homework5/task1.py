def get_unicode_num(symbol_ord: int) -> str:
    hexed = hex(symbol_ord)[2:].upper()
    return f"U+{'0'*(4-len(hexed))+hexed}"


def divide_equally(string: str, part_len: int, sep=" ") -> str:
    str_len = len(string)
    result = ""
    parts_count = str_len // part_len
    for i in range(1, parts_count + 1):
        result += string[part_len * (i - 1) : part_len * i] + (
            sep if i != parts_count else ""
        )
    return result


def get_bin_representation(symbol_ord: int) -> str:
    binned = bin(symbol_ord)[2:]
    if symbol_ord <= 65535:
        united_code = binned.rjust(16, "0")
        return divide_equally(united_code, 8)
    limited_ord_bin = bin(symbol_ord - 65536)[2:].rjust(20, "0")
    high_order = bin(int(limited_ord_bin[:10], 2) + 55296)[2:]
    low_order = bin(int(limited_ord_bin[10:], 2) + 56320)[2:]
    return divide_equally(high_order + low_order, 8)


def main() -> None:
    user_input = input("Enter a string: ")
    if not user_input:
        print("Enter something next time.")
        return
    print("UTF-16 encoding:")
    for symbol in user_input:
        symbol_ord = ord(symbol)
        print(
            "{}\t{}\t{}".format(
                symbol, get_unicode_num(symbol_ord), get_bin_representation(symbol_ord)
            )
        )


if __name__ == "__main__":
    main()
