import sys
from os.path import getsize


def wc(file_name, is_lines=True, is_words=True, is_bytes=True, is_count=False):
    result = ""
    file = open(file_name)
    lines = file.readlines()
    file.close()
    if is_lines:
        result += str(len(lines)) + " "
    if is_words:
        words_count = 0
        for line in lines:
            words_count += len(line.split())
        result += str(words_count) + " "
    if is_bytes:
        result += str(getsize(file_name))
    if is_count:
        chars_count = 0
        for line in lines:
            chars_count += len(line) if line != "\n" else 0
        result += str(chars_count)
    print(result[:-1])


def head_or_tail_n(file_name, head, n=10):
    file = open(file_name, "r")
    lines = [line for line in file]
    file.close()
    len_lines = len(lines)
    n = len_lines if len_lines < n else n
    for line in lines if head else lines[len_lines - n:]:
        print(line.rstrip())
        n -= 1
        if n <= 0:
            break


def head_or_tail_c(file_name, head, c):
    file = open(file_name, "r")
    lines = [line for line in file]
    file.close()
    lines = lines[::-1] if not head else lines
    file_encoding = file.encoding
    file.close()
    current_bytes = 0
    res = ""
    is_all_bytes_taken = False
    for line in lines:
        if is_all_bytes_taken:
            break
        for symbol in line if head else line[::-1]:
            current_symbol_bytes = len(symbol.encode(file_encoding)) if symbol != "\n" else 2
            if current_bytes + current_symbol_bytes <= c:
                res += symbol
                current_bytes += current_symbol_bytes
            else:
                is_all_bytes_taken = True
                break
    print(res) if head else print(res[::-1])


if __name__ == "__main__":
    input_info = sys.argv[1:]
    command = input_info[0]
    parameters = input_info[1:-1]
    given_file = input_info[-1]
    if command == "wc":
        if parameters:
            wc(given_file, "-l" in parameters, "-w" in parameters, "-c" in parameters, "-m" in parameters)
        else:
            wc(given_file)
    elif command == "head" or command == "tail":
        if "-n" in parameters:
            head_or_tail_n(given_file, command == "head", int(parameters[-1]))
        elif "-c" in parameters:
            head_or_tail_c(given_file, command == "head", int(parameters[-1]))
        if not parameters:
            head_or_tail_n(given_file, command == "head")
    else:
        print("Unknown command")
