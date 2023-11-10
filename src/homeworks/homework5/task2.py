def encode_string(string: str) -> str:
    if not string:
        raise ValueError("Given string is empty")
    if not string.isalpha():
        raise ValueError("Given string contains numbers or other unnecessary symbols")
    encoded = []
    start_i = 0
    string += "/"  # edge mark
    for i in range(len(string) - 1):
        if string[i] != string[i + 1]:
            encoded.append(f"{string[i]}{len(string[start_i:i + 1])}")
            start_i = i + 1
    return "".join(encoded)


def decode_string(string: str) -> str:
    if not string:
        raise ValueError("Given string is empty")
    if not string.isalnum():
        raise ValueError("Given string contains unnecessary symbols")
    letters = list(filter(lambda x: x.isalpha(), string))
    if not all(map(lambda x: len(x) == 1, letters)):
        raise ValueError(
            "Incorrect encoding format: more than one character before quantity"
        )
    counts = "".join(map(lambda x: x if x.isdigit() else " ", string)).split()
    if len(letters) != len(counts):
        raise ValueError(
            "Incorrect encoding format: letters amount dont match numbers amount"
        )
    return "".join(map(lambda x: x[0] * int(x[1]), zip(letters, counts)))


def represent_function(fun, user_string) -> str:
    try:
        result = fun(user_string)
    except ValueError as error:
        return f"{error}"
    return result


def main() -> None:
    user_select = input("Choose option:\n1.encode string\n2.decode string\n").rstrip(
        "."
    )
    if user_select == "1":
        print(
            represent_function(
                encode_string, input("Enter string you want to encode: ")
            )
        )
    elif user_select == "2":
        print(represent_function(decode_string, input("Enter encoded string: ")))
    else:
        print("Undefined option.")


if __name__ == "__main__":
    main()
