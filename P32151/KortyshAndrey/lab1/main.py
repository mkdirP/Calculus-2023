def check_diagonal_dominance(matrix) -> bool:
    strict: bool = False
    for i in range(len(matrix)):
        if sum([abs(j) for j in matrix[i]]) > 2 * abs(matrix[i][i]):
            return False
        if sum([abs(j) for j in matrix[i]]) < 2 * abs(matrix[i][i]):
            strict = True
    return strict


def get_diagonal_dominance(matrix):
    return sorted(matrix, key=lambda line: [abs(i) for i in line].index(max([abs(i) for i in line])))


def get_error_vector(old_x, new_x):
    return [abs(old_x[i] - new_x[i]) for i in range(len(old_x))]


def solution(dim, matrix, precision):
    A = [[matrix[j][i] for i in range(dim)] for j in range(dim)]
    B = [matrix[i][-1] for i in range(dim)]
    A = get_diagonal_dominance(A)
    if not check_diagonal_dominance(A):
        raise Exception
    coefficients = [[0 if i == j else -A[i][j] / A[i][i] for j in range(dim)] for i in range(dim)]
    free_coefficients = [B[i] / A[i][i] for i in range(dim)]
    x = free_coefficients.copy()
    cur_error = 1e9
    iterations = 0
    cur_error_vector = []
    while cur_error > precision:
        new_x = [free_coefficients[i] + sum(coefficients[i][j]*x[j] for j in range(dim)) for i in range(dim)]
        cur_error_vector = get_error_vector(x, new_x)
        cur_error = max(cur_error_vector)
        x = new_x
        iterations += 1
    return iterations, x, cur_error_vector


def main():
    n: str = "-1"
    while n != "0" and n != "1":
        n = input("Введите 0 для ввода с клавиатуры или 1 для ввода из файла: ")
    if n == "1":
        file = input("Введите название файла: ")
        try:
            with open(file, "r") as f:
                dim = int(f.readline())
                matrix = [[float(i) for i in f.readline().split()] for _ in range(dim)]
                precision = float(f.readline())
        except Exception as e:
            print("Неверные данные.")
            exit(0)
    else:
        try:
            dim = int(input("Введите размерность: "))
            print("Введите матрицу: ")
            matrix = [[float(i) for i in input().split()] for _ in range(dim)]
            precision = float(input("Введите точность: "))
        except Exception:
            print("Неверные данные.")
            exit(0)
    try:
        iterations, x, error = solution(dim, matrix, precision)
        print(f"Всего итераций {iterations}")
        print("Вектор неизвестных: ", *x)
        print("Вектор погрешностей: ", *error)
    except Exception:
        print("Диагональное преобразование не может быть достигнуто.")


if __name__ == "__main__":
    main()

# matrix1.txt
# matrix2.txt
