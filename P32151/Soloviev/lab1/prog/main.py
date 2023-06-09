import sys
import numpy as np
import pyfiglet


def print_matrix(matrix_a, matrix_b, dimension):
    print("\033[34m\033[40m{}".format("Original matrix:"))
    for i in range(dimension):
        for j in range(dimension + 1):
            if j < dimension:
                print('{:5}'.format(round(matrix_a[i][j], 3)), end=" ")
            else:
                print("|", '{:5}'.format(round(matrix_b[i][0], 3)))


def print_result_matrix(matrix, dimension):
    print("\033[35m{}".format("Triangle matrix:"))
    for i in range(dimension):
        for j in range(dimension + 1):
            if j < dimension:
                print("{:5}".format(round(matrix[i][j], 3)), end=" ")
            else:
                print("|", '{:5}'.format(round(matrix[i][j], 3)))


def enter_from_file(path):
    f = open(path)
    dimension = int(f.readline())
    matrix = np.eye(dimension, dimension + 1)
    matrix_a = np.eye(dimension)
    matrix_b = np.eye(dimension, 1)
    try:
        for i in range(dimension):
            matrix[i] = f.readline().split(" ")
    except:
        print("\033[31m{}".format("File error"))
        return None
    for i in range(dimension):
        for j in range(dimension):
            matrix_a[i][j] = matrix[i][j]
    for i in range(dimension):
        matrix_b[i][0] = matrix[i][dimension]
    return dimension, matrix_a, matrix_b


def enter_from_console(dimension):
    matrix = np.eye(dimension, dimension + 1)
    matrix_a = np.eye(dimension)
    matrix_b = np.eye(dimension, 1)
    print("Enter matrix rows:")
    try:
        for i in range(dimension):
            s = "row " + str(i + 1) + ": "
            matrix[i] = input(s).split(" ")
    except:
        print("\033[31m\033[40m{}".format("Invalid row. Re-enter the matrix"))

        return None
    for i in range(dimension):
        for j in range(dimension):
            matrix_a[i][j] = matrix[i][j]
    for i in range(dimension):
        matrix_b[i][0] = matrix[i][dimension]
    return matrix_a, matrix_b


def select_main_element(matrix_a, matrix_b, dimension):
    det = np.linalg.det(matrix_a)
    if round(det, 3) == 0:
        return None
    transformed_matrix = np.eye(dimension, dimension + 1)

    for i in range(dimension):
        for j in range(dimension + 1):
            if j < dimension:
                transformed_matrix[i][j] = matrix_a[i][j]
            else:
                transformed_matrix[i][j] = matrix_b[i][0]

    for i in range(dimension):
        max_i = i
        for m in range(i + 1, dimension):
            if abs(transformed_matrix[m][i]) > abs(transformed_matrix[max_i][i]):
                max_i = m

        # line permutation
        if max_i != i:
            for j in range(dimension + 1):
                transformed_matrix[i][j], transformed_matrix[max_i][j] = transformed_matrix[max_i][j], \
                                                                         transformed_matrix[i][j]

        # exclusion of the unknown
        for k in range(i + 1, dimension):
            coefficient = transformed_matrix[k][i] / transformed_matrix[i][i]
            for j in range(i, dimension + 1):
                transformed_matrix[k][j] -= coefficient * transformed_matrix[i][j]

    roots = np.linalg.solve(matrix_a, matrix_b)

    r = []
    for i in range(dimension):
        temp_r = 0
        for j in range(dimension + 1):
            if j < dimension:
                temp_r += transformed_matrix[i][j] * roots[j]
            else:
                temp_r -= transformed_matrix[i][j]
        r.append(temp_r)

    return det, transformed_matrix, roots, r


def main():
    hello_msg = pyfiglet.figlet_format("Matrix Solver")
    print("\033[31m{}".format(hello_msg))
    print("\033[31m\033[40m{}".format("Soloviev Artemiy P32151"))
    print("Task option 11")
    print("\033[0m".format())
    # to read from file run with key -f
    # in this form: python main.py -f *path*
    if len(sys.argv) == 3:
        if sys.argv[1] == "-f":
            from_file = enter_from_file(sys.argv[2])
            if from_file is None:
                return
            dimension, matrix_a, matrix_b = from_file
    else:
        while True:
            try:
                dimension = int(input("Enter dimension: "))
                if dimension > 20 or dimension < 1:
                    print("\033[31m{}".format("dimension must be between 1 and 20"))
                    print("\033[0m".format())
                else:
                    break
            except:
                print("dimension must be number between 1 and 20")
                pass
        matrix_a, matrix_b = enter_from_console(dimension)

    print_matrix(matrix_a, matrix_b, dimension)
    ans = select_main_element(matrix_a, matrix_b, dimension)
    if ans is None:
        print("\033[31m{}".format("Determinant = 0. Matrix is inconsistent"))
        print("\033[0m".format())
        return
    det, transformed_matrix, roots, r = ans
    print_result_matrix(transformed_matrix, dimension)
    print("\033[33m{}".format("Determinant ="), round(det, 3))
    print("\033[32m{}".format("Roots:"))
    for i in range(len(roots)):
        root = float(roots[i])
        print("x_", end='')
        print(i + 1, "=", round(root, 3))
    print("\033[36m{}".format("Errors:"))
    for i in range(len(r)):
        print(round(float(r[i]),3))


if __name__ == '__main__':
    main()
