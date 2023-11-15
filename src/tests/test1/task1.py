import sys
from os.path import exists


def count_letters(text):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    counter = dict()
    for symbol in text:
        if symbol in letters:
            counter[symbol] = counter.get(symbol, 0) + 1
    return counter


def get_file_text(file_path):
    file_text = ""
    with open(file_path, "r") as f_in:
        for line in f_in:
            file_text += line
    return file_text


def sort_dict_keys_by_ord(dictionary: dict):
    return sorted(dictionary, key=lambda key: ord(key))


def write_counted_letters(file_path, sorted_letters: list, letter_count: dict):
    with open(file_path, "w") as f_out:
        for letter in sorted_letters:
            f_out.write(f"{letter}: {letter_count[letter]}")
            f_out.write("\n" if letter != sorted_letters[-1] else "")


def main():
    user_input = sys.argv
    input_file, output_file = user_input[1], user_input[2]
    if not exists(input_file):
        print("Файл с данными не найден!")
        return
    if exists(output_file):
        print("Файл для результатов уже существует!")
        return
    raw_text = get_file_text(input_file)
    counted = count_letters(raw_text)
    order = sort_dict_keys_by_ord(counted)
    write_counted_letters(output_file, order, counted)


if __name__ == "__main__":
    main()
