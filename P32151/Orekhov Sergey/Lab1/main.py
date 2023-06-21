import calculatings

print("Файл для данных матрицы находится в папке resources и называется matrix.txt.")
print("Выберете тип ввода, консоль(напишите 1) или из файла(напишите 2):")

start_matrix = []

type_of_input = input()
if type_of_input == "1":
    try:
        print("Введите epsilon через точку:")
        eps = float(input())
        print("Введите целое N: ")
        n = int(input())
        print("Введите целое M: ")
        m = int(input())
    except Exception:
        print("Некорректные параметры матрицы")
        exit()
    print("Введите данные матрицы(построчно, в строке через пробел):")
    try:
        start_matrix = [[0] * (n + 1)] * n
        for i in range(n):
            str_of_matrix = input().split(" ")
            for j in range(len(str_of_matrix)):
                start_matrix[i][j] = float(str_of_matrix[j])
            start_matrix[i] = str_of_matrix
    except Exception:
        print("Некорректные данные матрицы")
        exit()


elif type_of_input == "2":
    with open("resources/matrix.txt") as f:
        file_matrix = f.readlines()
        for i in range(len(file_matrix)):
            if i == 0:
                continue
            elif i == 1:
                try:
                    str_of_matrix = file_matrix[i][:-2].split(" ")
                    eps = float(str_of_matrix[0])
                    n = int(str_of_matrix[1])
                    m = int(str_of_matrix[2])
                except Exception:
                    print("Некорректные параметры матрицы")
                    exit()
            else:
                try:

                    if i == len(file_matrix) - 1:
                        str_of_matrix = file_matrix[i].split(" ")
                    else:
                        str_of_matrix = file_matrix[i].split(" ")
                    for j in range(len(str_of_matrix)):
                        str_of_matrix[j] = float(str_of_matrix[j])
                    start_matrix.append(str_of_matrix)
                except Exception:
                    print(str_of_matrix)
                    print("Некорректные данные матрицы")
                    exit()
else:
    print("Введён некорректный тип ввода данных")
    exit()

calculatings.SIZE = n
calculatings.epsilon = eps
calculatings.M = m
calculatings.setMatrixAandB(start_matrix)
calculatings.initX1andX2()
calculatings.startCalculating()
