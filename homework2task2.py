import csv
from os.path import exists


def determine_word_frequency(file_name, file_encoding="utf-8"):
    word_to_frequency = dict()
    with open(file_name, "r", encoding=file_encoding) as f_in:
        for line in f_in:
            split_line = line.lower().split()
            for word in split_line:
                word_to_frequency[word] = word_to_frequency.get(word, 0) + 1
    return word_to_frequency


def write_csv_word_frequency(file_name, dict_data, file_encoding="utf-8"):
    with open(file_name, "w", encoding=file_encoding) as csv_f_in:
        writer = csv.writer(csv_f_in, quoting=csv.QUOTE_NONNUMERIC)
        writer.writerow(["Слово", "Частота Встречаемости"])
        writer.writerows(dict_data.items())


if __name__ == "__main__":
    user_txt_file_name = input("Введите путь до txt файла, в котором нужно  посчитать частоту встречаемости каждого"
                               " уникального слова: ")
    if exists(user_txt_file_name):
        data = determine_word_frequency(user_txt_file_name)
        user_csv_file_name = input("Введите путь до пустого csv файла, в который будет записан результат (если файла"
                                   " нет, то он будет создан): ")
        write_csv_word_frequency(user_csv_file_name, data)
    else:
        print("txt файл не найден")
