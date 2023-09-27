from math import sqrt, acos, degrees


def get_vector_length(vector):
    return sqrt(sum([coord**2 for coord in vector]))


def get_scalar_product(vector1, vector2):
    return sum([vector1[i] * vector2[i] for i in range(len(vector1))])


def get_angle_between_vectors(vector1, vector2):
    return degrees(
        acos(
            get_scalar_product(vector1, vector2)
            / (get_vector_length(vector1) * get_vector_length(vector2))
        )
    )


def get_transposed_matrix(matrix, rows_count, columns_count):
    return [[matrix[j][i] for j in range(rows_count)] for i in range(columns_count)]


def get_matrices_sum(matrix1, matrix2, rows_count, columns_count):
    return [
        [matrix1[j][i] + matrix2[j][i] for i in range(columns_count)]
        for j in range(rows_count)
    ]


def get_matrices_product(
    matrix1, matrix2, rows_count1, columns_count1, rows_count2, columns_count2
):
    if columns_count1 != rows_count2:
        return None
    transposed_matrix2 = get_transposed_matrix(matrix2, rows_count2, columns_count2)
    return [
        [
            get_scalar_product(matrix1[i], transposed_matrix2[j])
            for j in range(columns_count2)
        ]
        for i in range(rows_count1)
    ]


def get_vector_from_user(vector_name=""):
    raw_vector = input(
        "Enter {}vector coordinates in format\nA1,A2,...An where each 'A' is coordinate in another "
        "dimension:\n".format(vector_name)
    )
    processed_vector = [int(coord) for coord in raw_vector.split(",")]
    return processed_vector


def get_matrix_info_from_user(matrix_name=""):
    matrix_rows_count = int(
        input("Enter number of {}matrix rows: ".format(matrix_name))
    )
    matrix_columns_count = int(
        input("Enter number of {}matrix columns: ".format(matrix_name))
    )
    matrix = []
    for row_num in range(1, matrix_rows_count + 1):
        matrix.append(
            [
                int(element)
                for element in input(
                    "Enter {} row of {}matrix, in format"
                    " B1,B2,...Bn where each 'B' is matrix"
                    " element: ".format(row_num, matrix_name)
                ).split(",")
            ]
        )
    return [matrix, matrix_rows_count, matrix_columns_count]


def get_answer_from_vectors_menu(chosen_option):
    given_vector1 = get_vector_from_user("first ")
    if chosen_option == "1":
        return "Vector length: {}".format(get_vector_length(given_vector1))
    elif chosen_option == "2":
        given_vector2 = get_vector_from_user("second ")
        return "scalar product: {}".format(
            get_scalar_product(given_vector1, given_vector2)
        )
    elif chosen_option == "3":
        given_vector2 = get_vector_from_user("second ")
        return "Angle between vectors: {} degrees".format(
            get_angle_between_vectors(given_vector1, given_vector2)
        )


def get_answer_from_matrices_menu(chosen_option):
    matrix1_info = get_matrix_info_from_user("first ")
    if chosen_option == "1":
        transposed = get_transposed_matrix(
            matrix1_info[0], matrix1_info[1], matrix1_info[2]
        )
        return transposed
    elif chosen_option == "2":
        print("Both matrices must be the same size!")
        matrix2_info = get_matrix_info_from_user("second ")
        sum_matrix = get_matrices_sum(
            matrix1_info[0], matrix2_info[0], matrix1_info[1], matrix1_info[2]
        )
        return sum_matrix
    elif chosen_option == "3":
        print(
            "The number of columns in the first matrix must match the number of rows in the second matrix!"
        )
        matrix2_info = get_matrix_info_from_user("second ")
        product_matrix = get_matrices_product(
            matrix1_info[0],
            matrix2_info[0],
            matrix1_info[1],
            matrix1_info[2],
            matrix2_info[1],
            matrix2_info[2],
        )
        return product_matrix


if __name__ == "__main__":
    condition = "welcome"
    while condition != "exit":
        if condition == "welcome":
            condition = input(
                "Select what you want to operate with:\n1.Vectors\n2.Matrices\n3.Nothing\n"
            )
        elif condition == "1":
            action = input(
                "Select operation:\n1.Define vector length\n2.Calculate scalar product\n3.Define angle "
                "between vectors\n4.Back\n"
            )
            if action == "4":
                condition = "welcome"
                continue
            print(get_answer_from_vectors_menu(action))
        elif condition == "2":
            action = input(
                "Select operation:\n1.Transpose matrix\n2.Calculate sum of matrices \n3.Calculate"
                " product of matrices\n4.Back\n"
            )
            if action == "4":
                condition = "welcome"
                continue
            calculated_matrix = get_answer_from_matrices_menu(action)
            print("Result:")
            for row in calculated_matrix:
                print(row)
        elif condition == "3":
            print("Bye.")
            condition = "exit"
