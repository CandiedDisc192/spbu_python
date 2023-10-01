from os.path import exists


def find_list_fragment(lst, fragment, searching_start_index=0):
    length_of_fragment = len(fragment)
    for i in range(searching_start_index, len(lst) - length_of_fragment + 1):
        if fragment == lst[i : i + length_of_fragment]:
            return i, i + length_of_fragment - 1


def delete_list_fragment(lst, start_sequence, end_sequence):
    indexes_of_start = find_list_fragment(lst, start_sequence)
    indexes_of_end = find_list_fragment(lst, end_sequence, indexes_of_start[1] + 1)
    return lst[: indexes_of_start[0]] + lst[indexes_of_end[1] + 1 :]


def list_insert_fragment(lst, start_sequence, fragment):
    end_index_of_start = find_list_fragment(lst, start_sequence)[1]
    return lst[: end_index_of_start + 1] + fragment + lst[end_index_of_start + 1 :]


def list_replace_fragment(lst, template, fragment):
    temporary_list = list_insert_fragment(lst, template, fragment)
    return delete_list_fragment(temporary_list, template, [])


def transform_logs(logs_file_path, transformed_logs_file_path):
    transforming_file = open(transformed_logs_file_path, "w", encoding="utf-8")
    with open(logs_file_path, "r", encoding="utf-8") as logs_f_in:
        origin_dna_length = int(logs_f_in.readline())
        raw_dna = logs_f_in.readline()
        dna = [raw_dna[i] for i in range(origin_dna_length)]
        logs_count = int(logs_f_in.readline())
        for raw_log_i in range(logs_count):
            log = logs_f_in.readline().split()
            if log[0] == "DELETE":
                dna = delete_list_fragment(
                    dna,
                    [chemical_compound for chemical_compound in log[1]],
                    [chemical_compound for chemical_compound in log[2]],
                )
            elif log[0] == "INSERT":
                dna = list_insert_fragment(
                    dna,
                    [chemical_compound for chemical_compound in log[1]],
                    [chemical_compound for chemical_compound in log[2]],
                )
            elif log[0] == "REPLACE":
                dna = list_replace_fragment(
                    dna,
                    [chemical_compound for chemical_compound in log[1]],
                    [chemical_compound for chemical_compound in log[2]],
                )
            transforming_file.write(
                "".join(dna) + "\n"
            ) if raw_log_i != logs_count - 1 else transforming_file.write("".join(dna))
        transforming_file.close()


if __name__ == "__main__":
    user_logs_file_path = input("Введите путь до txt файла с данными эксперементов: ")
    if exists(user_logs_file_path):
        user_result_file_path = input(
            "Введите путь до пустого txt файла, в который будет записан результат (если файла"
            " нет, то он будет создан): "
        )
        transform_logs(user_logs_file_path, user_result_file_path)
    else:
        print("Файл не найден.")
