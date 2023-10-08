from os.path import exists


def get_current_dna(origin_dna, current_log):
    command, arg1, arg2 = current_log
    if command == "DELETE":
        start_index = origin_dna.find(arg1)
        end_index = origin_dna.find(arg2, start_index + len(arg1)) + len(arg2)
        origin_dna = origin_dna[:start_index] + origin_dna[end_index:]
    elif command == "INSERT":
        insert_index = origin_dna.find(arg1) + len(arg1)
        origin_dna = origin_dna[:insert_index] + arg2 + origin_dna[insert_index:]
    elif command == "REPLACE":
        origin_dna = origin_dna.replace(arg1, arg2, 1)
    return origin_dna


def transform_logs(logs_file_path, transformed_logs_file_path):
    transformed_lines = []
    with open(logs_file_path, "r", encoding="utf-8") as logs_f_in:
        _ = int(logs_f_in.readline())
        dna = logs_f_in.readline().rstrip()
        logs_count = int(logs_f_in.readline())
        for raw_log_i in range(logs_count):
            dna = get_current_dna(dna, logs_f_in.readline().split())
            transformed_lines.append(dna + "\n" if raw_log_i != logs_count - 1 else dna)
    with open(transformed_logs_file_path, "w", encoding="utf-8") as transforming_file:
        transforming_file.writelines(transformed_lines)


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
