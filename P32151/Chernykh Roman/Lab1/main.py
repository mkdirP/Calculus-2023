import numpy as np

def get_triangle(sz, matrix):
    try:
        print("Изначальная матрица:\n")

        mtx_original = np.array(matrix)
        print(mtx_original)
        mtx = np.array(matrix)

        determinant = round(np.linalg.det(np.delete(mtx_original, -1, 1)), 3)
        if round(determinant, 3) == 0:
            print("Определитель равен 0 ;(")
            exit()
        s = 0

        n = len(matrix)
        # Прямой ход
        for i in range(n - 1):
            # Поиск максимального элемента в столбце
            max_i = i
            for m in range(i + 1, n):
                if abs(matrix[m][i]) > abs(matrix[max_i][i]):
                    max_i = m

            # Перестановка строк
            if max_i != i:
                for j in range(n + 1):
                    matrix[i][j], matrix[max_i][j] = matrix[max_i][j], matrix[i][j]

            # Исключение i-того неизвестного
            for k in range(i + 1, n):
                coef = matrix[k][i] / matrix[i][i]
                for j in range(i, n + 1):
                    matrix[k][j] -= coef * matrix[i][j]


        korni = np.linalg.solve(mtx_original[:, :-1], mtx_original[:, -1])

        nevyazka = [0] * n
        for i in range(n):
            s_part = 0
            for j in range(n):
                s_part += matrix[i][j] * korni[j]
            nevyazka[i] = s_part - matrix[i][n]

        mtv = np.array(matrix)
        nev = np.array(nevyazka)

        return determinant, mtv, nev, korni
    except ValueError:
        print("Неправильный формат ввода. Попробуйте снова ...")
        exit(0)

def start(sz, matrix):
    return get_triangle(sz, matrix)


def read_console():
    try:
        size = int(input("Введите размерность матрицы:"))
        if size == 1:
            print("Размерность не может быть равна одному")
        else:
            print("Введите матрицу через пробел в формате: \nA11 ... A1" + str(size) + " B1\n... \nA" + str(size)
                  + "1 ... A" + str(size) + "" + str(size) + " B" + str(size))
            matrix = [[float(i) for i in input().split()] for _ in range(size)]

            return size, matrix

    except ValueError:
        print("Неправильный формат ввода. Попробуйте снова ...")
        exit(0)
    return 0,

def read_file():
    file = input("Введите название файла: ")
    try:
        with open(file, "r") as f:
            size = int(f.readline())
            matrix = [[float(i) for i in f.readline().split()] for _ in range(size)]
            return size, matrix
    except Exception as e:
        print("Неверные данные.")
        exit(0)


def main():
    choose = input("Введите \"1\" для ввода данных с консоли, либо \"2\" "
                   "для ввода данных из файла \n")

    while not (choose == "1" or choose == "2"):
        choose = input("Введены некоректные данный :( \nВведите \"1\" "
                       "для ввода данных с консоли, либо \"2\" для ввода данных из файла\n")

    if choose == "1":
        sz, mtx = read_console()
        determinant, mtx, nevyazka, korni = start(sz,mtx)
        print(f"Детерминант = \n {determinant}  \n")
        print(f"Треугольная матрица: \n {mtx}  \n")
        print(f"Корни: \n {korni}  \n")
        print(f"Невязочка = \n {nevyazka}  \n")
        return
    else:
        sz, mtx = read_file()
        determinant, mtx, nevyazka, korni = start(sz, mtx)
        print(f"Детерминант = \n {determinant}  \n")
        print(f"Треугольная матрица: \n {mtx}  \n")
        print(f"Корни: \n {korni}  \n")
        print(f"Невязочка = \n {nevyazka}  \n")
        return

if __name__ == '__main__':
    main()
