import sys
import numpy as np

def matrix_parser(size):
    main_mas = []
    for i in range(size):
        string = input()
        mas = []
        for j in range(1, size + 1):
            x = "x" + str(j)
            start = string.find(x)
            if start != -1:
                num = 1
                end_plus = string.rfind("+", 0, start)
                end_minus = string.rfind("-", 0, start)
                if end_plus != -1 and end_plus > end_minus:
                    if end_plus + 1 == start:
                        num = 1
                    else:
                        num = float(string[end_plus + 1:start])
                elif end_minus != -1 and end_plus < end_minus:
                    if end_minus + 1 == start:
                        num = -1
                    else:
                        num = -float(string[end_minus + 1:start])
                else:
                    num = string[0:start]
                if start == 0:
                    num = 1
                mas.append(float(num))
            else:
                mas.append(float(0))
        mas.append(float(string[string.find("=") + 1:len(string)]))
        main_mas.append(mas)
    main_mas = np.array(main_mas)
    return main_mas

def gaussFunc(matrix):
    matrix = np.array(matrix)
    for nrow, row in enumerate(matrix):
        divider = row[nrow]
        if abs(divider) < 1e-10:
            print(f"Матрица несовместна. Максимальный элемент в столбце {nrow}: {divider:.3g}")
            sys.exit()
        row /= divider
        for lower_row in matrix[nrow + 1:]:
            factor = lower_row[nrow]
            lower_row -= factor * row
    return matrix

def main_log(main_mas):
    main_mas = np.array(main_mas)
    print("\nОпределитель: " + np.linalg.det(main_mas[:main_mas.__len__(), :main_mas.__len__()]).__str__())
    main_mas = gaussFunc(main_mas)

    print("Диагональная матрица:")
    for i in range(main_mas.__len__()):
        for l in range(main_mas[0].__len__()):
            print(f'{main_mas[i][l].__str__() + " ":>5}', end="")
        print("")
    res = make_identity(main_mas)[:, 3]
    print("Результаты:")
    for i in res:
        print(f'{i:>5}', end="")
    print("")
    print("Вязкость:")
    for i in range(main_mas.__len__()):
        a = main_mas[i][main_mas.__len__()]
        for l in range(main_mas.__len__()):
            a=a-main_mas[i][l]*res[l]
        print(f'{a:>5}', end="")

def make_identity(matrix):
    for nrow in range(len(matrix) - 1, 0, -1):
        row = matrix[nrow]
        for upper_row in matrix[:nrow]:
            factor = upper_row[nrow]
            upper_row -= factor * row
    return matrix

if __name__ == '__main__':
    print("\033[93m{}\033[0m".format("Горинов Даниил Андреевич\n"
                                     "Вариант 3\n"
                                     "Метод Гаусса"))
    a = input('C-консольный, F-файловый.\n')
    while a != "C" and a != "F":
        a = input('Не правильно, попробуйте снова.\n')
    if a == "C":
        size = input('Введите размерность системы:\n')
        while not(size.isdigit()) or int(size) > 20 or int(size) < 0:
            size = input('Не правильно, попробуйте снова.\n')
        size = int(size)
        print("Пример ввода системы уравнений:\n",
              "1x1+2x2+3x3=0\n",
              "1x1+2x2+3x3=0\n",
              "1x1+2x2+3x3=0")
        print("Введите систему:")
        try:
            main_mas = matrix_parser(size)
        except Exception:
            print("\033[31m{}\033[0m".format("Ошибка парсинга файла."))
            sys.exit()
        main_log(main_mas)
    else:
        path = input('Введите путь к файлу:\n')
        try:
            File = open(path, 'r')
            size = int(File.readline())
            main_mas = matrix_parser(size)
            main_log(main_mas)
        except FileNotFoundError:
            print("\033[31m{}\033[0m".format("Путь указан неверно, попробуйте снова"))
            sys.exit()
