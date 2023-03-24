import sys

def input_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            break
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите целое число.")
    return value

def input_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            break
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите число с плавающей точкой.")
    return value


def input_float_list(prompt):
    while True:
        try:
            value = list(map(float, input(prompt).split()))
            break
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите список чисел с плавающей точкой.")
    return value

def read_data_from_file(file_name):
    try:
        with open(file_name, 'r') as file:
            n = int(file.readline().strip())
            matrix = [list(map(float, file.readline().strip().split())) for _ in range(n)]
            rhs = list(map(float, file.readline().strip().split()))
            precision = float(file.readline().strip())
        return n, matrix, rhs, precision
    except FileNotFoundError:
        print("Ошибка: файл не найден.")
        return None
    except ValueError:
        print("Ошибка: некорректные данные в файле.")
        return None
    except Exception as e:
        print("Ошибка: произошла ошибка при чтении файла:", e)
        return None


def read_data_from_keyboard():
    n = input_int("Введите размерность матрицы n: ")
    matrix = []
    print("Введите матрицу A:")
    for _ in range(n):
        row = input_float_list("Введите строку матрицы: ")
        matrix.append(row)
    print("Введите вектор правой части b:")
    rhs = input_float_list("Введите элементы вектора правой части: ")
    precision = input_float("Введите точность (например: 0.01): ")
    return n, matrix, rhs, precision

def swap_rows(matrix, row1, row2):
    matrix[row1], matrix[row2] = matrix[row2], matrix[row1]

def swap_columns(matrix, col1, col2):
    for row in matrix:
        row[col1], row[col2] = row[col2], row[col1]

def check_diagonal_dominance(matrix):
    n = len(matrix)
    strict_dominance = False
    for i in range(n):
        diagonal_element = abs(matrix[i][i])
        sum_of_others = sum(abs(matrix[i][j]) for j in range(n) if j != i)
        if diagonal_element < sum_of_others:
            return False
        if diagonal_element > sum_of_others:
            strict_dominance = True
    return strict_dominance

def find_max_diagonal_entry(matrix, size, index):
    max_value = abs(matrix[index][index])
    max_row = index
    max_col = index

    for i in range(index, size):
        for j in range(index, size):
            if abs(matrix[i][j]) > max_value:
                max_value = abs(matrix[i][j])
                max_row = i
                max_col = j

    return max_row, max_col

def diagonal_dominance(matrix):
    if check_diagonal_dominance(matrix):
        return True
        
    n = len(matrix)
    for k in range(n):
        i, j = find_max_diagonal_entry(matrix, len(matrix), k)
        if matrix[i][j] == 0:
            return False
        swap_rows(matrix, k, i)
        swap_columns(matrix, k, j)
        
        if check_diagonal_dominance(matrix):
            return True

    return False

def simple_iterations(matrix, rhs, precision):
    n = len(matrix)
    x = [0] * n
    error = [0] * n
    iteration_count = 0

    while True:
        new_x = [0] * n
        for i in range(n):
            s = sum(matrix[i][j] * x[j] for j in range(n) if j != i)
            new_x[i] = (rhs[i] - s) / matrix[i][i]

        error = [abs(new_x[i] - x[i]) for i in range(n)]
        if max(error) < precision:
            break

        x = new_x
        iteration_count += 1

    return x, error, iteration_count

def main():
    print("Привет пользователь, эта программа предназначена для решения систем линейных уравнений методом простых итераций.\nОна не найдет точное решение, но найдет решение с заданной тобою точностью")
    print("Выберите способ ввода данных:")
    print("1 - Ввод с клавиатуры")
    print("2 - Чтение из файла")
    choice = input_int("Введите номер выбранного варианта: ")

    if choice == 1:
        n, matrix, rhs, precision = read_data_from_keyboard()
    elif choice == 2:
        file_name = input("Введите имя файла с данными: ")
        data = read_data_from_file(file_name)
        if data is None:
            print("Операция прервана из-за ошибки.")
            return
        n, matrix, rhs, precision = data
    else:
        print("Неправильный выбор")
        return

    if diagonal_dominance(matrix):
        print("Матрица после преобразования (если было выполнено):")
        for row in matrix:
            print(row)

        x, error, iteration_count = simple_iterations(matrix, rhs, precision)
        print("Вектор решения: ", x)
        print("Количество итераций: ", iteration_count)
        print("Вектор погрешностей: ", error)
    else:
        print("Не удалось привести матрицу к виду с диагональным преобладанием")

def handle_uncaught_exception(exc_type, exc_value, exc_traceback):
    print("Непредвиденная ошибка:", exc_value)

if __name__ == "__main__":
    sys.excepthook = handle_uncaught_exception
    main()