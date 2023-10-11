import sys
from os.path import exists


def get_file_numbers(file_path):
    with open(file_path, "r") as f_in:
        raw_numbers = f_in.readline().split()
    return [int(num) for num in raw_numbers]


def write_in_order(num1, num2, f_in_numbers, new_file_path):
    ordered_data = [[], [], []]
    for num in f_in_numbers:
        if num < num1:
            ordered_data[0].append(str(num))
        elif num1 <= num <= num2:
            ordered_data[1].append(str(num))
        else:
            ordered_data[2].append(str(num))
    with open(new_file_path, "w") as f_out:
        f_out.write(" ".join(ordered_data[0]) + "\n")
        f_out.write(" ".join(ordered_data[1]) + "\n")
        f_out.write(" ".join(ordered_data[2]))


if __name__ == "__main__":
    user_input = sys.argv
    a, b = int(user_input[1]), int(user_input[2])
    f, g = user_input[3], user_input[4]

    if not exists(f):
        print(f"Файл {f} не найден")
    elif exists(g):
        print(f"Файл {g} уже сушествует")
    else:
        numbers = get_file_numbers(f)
        write_in_order(a, b, numbers, g)
        print("Выполнено")
