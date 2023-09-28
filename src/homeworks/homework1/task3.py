import sys


def wc(file_name):
    result = {"-l": 0, "-w": 0, "-c": 0, "-m": 0}
    with open(file_name, "r") as file:
        file_encoding = file.encoding
        for line in file:
            result["-l"] += 1
            result["-w"] += len(line.split())
            result["-m"] += len(line)
            result["-c"] += len(line.encode(file_encoding)) + (line[-1] == "\n")
    return result


def head_or_tail_n(file_name, is_head, n=10):
    file = open(file_name, "r")
    lines = [line for line in file]
    lines = lines[::-1] if not is_head else lines
    file.close()
    len_lines = len(lines)
    n = len_lines if len_lines < n else n
    result = []
    for i in range(n):
        result.append(lines[i])
    return "".join(result) if is_head else "".join(result[::-1])


def head_or_tail_c(file_name, is_head, c):
    file = open(file_name, "r")
    lines = [line for line in file]
    file.close()
    lines = lines[::-1] if not is_head else lines
    file_encoding = file.encoding
    file.close()
    current_bytes = 0
    res = ""
    for line in lines:
        line = line[::-1] if not is_head else line
        encoded_line = line.encode(file_encoding)
        bytes_taken_by_line = len(encoded_line) + ("\n" in line)
        if current_bytes + bytes_taken_by_line > c:
            for symbol in line:
                symbol_bytes = len(symbol.encode(file_encoding)) + (symbol == "\n")
                if current_bytes + symbol_bytes <= c:
                    res += symbol
                    current_bytes += symbol_bytes
                else:
                    break
            break
        else:
            res += line
            current_bytes += bytes_taken_by_line
    return res if is_head else res[::-1]


if __name__ == "__main__":
    input_info = sys.argv[1:]
    command = input_info[0]
    user_parameters = input_info[1:-1]
    given_file = input_info[-1]

    if command == "wc":
        wc_result = wc(given_file)
        if user_parameters:
            order = ["-l", "-w", "-c", "-m"]
            output = ""
            for parameter in order:
                if parameter in user_parameters:
                    print(wc_result[parameter], end=" ")
        else:
            print(wc_result["-l"], wc_result["-w"], wc_result["-c"])

    elif command == "head" or command == "tail":
        if "-n" in user_parameters:
            print(
                head_or_tail_n(given_file, command == "head", int(user_parameters[-1]))
            )
        elif "-c" in user_parameters:
            print(
                head_or_tail_c(given_file, command == "head", int(user_parameters[-1]))
            )
        if not user_parameters:
            print(head_or_tail_n(given_file, command == "head"))

    else:
        print("Unknown command")
