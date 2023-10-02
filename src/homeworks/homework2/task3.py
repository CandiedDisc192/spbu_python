from os.path import exists


def transform_logs(logs_file_path, transformed_logs_file_path):
    transformed_text = ""
    with open(logs_file_path, "r", encoding="utf-8") as logs_f_in:
        origin_dna_length, dna, logs_count = (
            int(logs_f_in.readline()),
            logs_f_in.readline().rstrip(),
            int(logs_f_in.readline()),
        )
        for raw_log_i in range(logs_count):
            log = logs_f_in.readline().split()
            if log[0] == "DELETE":
                start_index = dna.find(log[1])
                end_index = dna.find(log[2], start_index + len(log[1])) + len(log[2])
                dna = dna[:start_index] + dna[end_index:]
            elif log[0] == "INSERT":
                insert_index = dna.find(log[1]) + len(log[1])
                dna = dna[:insert_index] + log[2] + dna[insert_index:]
            elif log[0] == "REPLACE":
                dna = dna.replace(log[1], log[2], 1)
            transformed_text += dna + "\n" if raw_log_i != logs_count - 1 else dna
        with open(
            transformed_logs_file_path, "w", encoding="utf-8"
        ) as transforming_file:
            transforming_file.write(transformed_text)


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
