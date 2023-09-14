from math import sqrt, acos, degrees


def get_vector_length(vector):
    return sqrt(sum([coord ** 2 for coord in vector]))


def get_dot_product(vector1, vector2):
    return sum([vector1[i] * vector2[i] for i in range(len(vector1))])


def get_angle_between_vectors(vector1, vector2):
    return degrees(acos(get_dot_product(vector1, vector2) / (get_vector_length(vector1) * get_vector_length(vector2))))


def get_transposed_matrix(matrix, rows_count, columns_count):
    transposed_matrix = [[0] * rows_count for _ in range(columns_count)]
    for ri in range(rows_count):
        for ci in range(columns_count):
            transposed_matrix[ci][ri] = matrix[ri][ci]
    return transposed_matrix


def get_matrices_sum(matrix1, matrix2, rows_count, columns_count):
    res = [[0] * columns_count for _ in range(rows_count)]
    for ri in range(rows_count):
        for ci in range(columns_count):
            res[ri][ci] = matrix1[ri][ci] + matrix2[ri][ci]
    return res


def get_matrices_product(matrix1, matrix2, rows_count1, columns_count1, rows_count2, columns_count2):
    if columns_count1 != rows_count2:
        return None
    product = [[0] * columns_count2 for _ in range(rows_count1)]
    for ri in range(rows_count1):
        for ci in range(columns_count2):
            for ti in range(columns_count1):
                product[ri][ci] += matrix1[ri][ti] * matrix2[ti][ci]
    return product


def get_vector_from_user(vector_name=""):
    raw_vector = input("Enter {}vector coordinates in format\nA1,A2,...An where each 'A' is coordinate in another "
                       "dimension:\n".format(vector_name))
    processed_vector = [int(coord) for coord in raw_vector.split(",")]
    return processed_vector


def get_matrix_info(matrix_name=""):
    matrix_rows_count = int(input("Enter number of {}matrix rows: ".format(matrix_name)))
    matrix_columns_count = int(input("Enter number of {}matrix columns: ".format(matrix_name)))
    matrix = []
    for row_num in range(1, matrix_rows_count+1):
        matrix.append([int(element) for element in input("Enter {} row of {}matrix, in format"
                                                         " B1,B2,...Bn where each 'B' is matrix"
                                                         " element: ".format(row_num, matrix_name)).split(",")])
    return [matrix, matrix_rows_count, matrix_columns_count]


if __name__ == "__main__":
    condition = "welcome"
    while condition != "exit":
        if condition == "welcome":
            condition = input("Select what you want to operate with:\n1.Vectors\n2.Matrices\n3.Nothing\n")

        elif condition == "1":
            action = input("Select operation:\n1.Define vector length\n2.Calculate dot product\n3.Define angle between "
                           "vectors\n4.Back\n")
            if action == "1":
                given_vector = get_vector_from_user()
                print("Vector length: {}".format(get_vector_length(given_vector)))
            elif action == "2":
                given_vector1 = get_vector_from_user("first ")
                given_vector2 = get_vector_from_user("second ")
                print("Dot product: {}".format(get_dot_product(given_vector1, given_vector2)))
            elif action == "3":
                given_vector1 = get_vector_from_user("first ")
                given_vector2 = get_vector_from_user("second ")
                print("Angle between vectors: {} degrees".format(get_angle_between_vectors(given_vector1, given_vector2)))
            elif action == "4":
                condition = "welcome"

        elif condition == "2":
            action = input("Select operation:\n1.Transpose matrix\n2.Calculate sum of matrices \n3.Calculate"
                           " product of matrices\n4.Back\n")
            if action == "1":
                matrix_info = get_matrix_info()
                transposed = get_transposed_matrix(matrix_info[0], matrix_info[1], matrix_info[2])
                print("Transposed matrix:")
                for row in transposed:
                    print(row)
            elif action == "2":
                print("Both matrices must be the same size!")
                matrix1_info = get_matrix_info("first ")
                matrix2_info = get_matrix_info("second ")
                sum_matrix = get_matrices_sum(matrix1_info[0], matrix2_info[0], matrix1_info[1], matrix1_info[2])
                print("Addition result:")
                for row in sum_matrix:
                    print(row)
            elif action == "3":
                print("The number of columns in the first matrix must match the number of rows in the second matrix!")
                matrix1_info = get_matrix_info("first ")
                matrix2_info = get_matrix_info("second ")
                product_matrix = get_matrices_product(matrix1_info[0], matrix2_info[0], matrix1_info[1], matrix1_info[2],
                                                      matrix2_info[1], matrix2_info[2])
                print("Product:")
                for row in product_matrix:
                    print(row)
            elif action == "4":
                condition = "welcome"

        elif condition == "3":
            print("Bye.")
            condition = "exit"
