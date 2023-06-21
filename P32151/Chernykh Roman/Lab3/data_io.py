import functions as fn


def get_function_num():
    num = -1
    while num != 1 and num != 2 and num != 3:
        for i in range(1, 4):
            print(str(i) + ") " + fn.get_function_name(i) + ";")
        try:
            num = int(input("Введите номер желаемой функции: "))
        except ValueError:
            print("Номер функции должен быть числом")
    return num


def get_interval():
    while True:
        try:
            a, b = map(float, input("Ведите границы интервала через пробел: ").split())
            if a == b:
                print("Введите разные числа: ")
                continue
            break
        except ValueError:
            print("Границы интервала должны быть числами, введёнными через пробел")
    return a, b


def ask_method():
    type = 0
    while type != 1 and type != 2 and type != 3 and type != 4 and type != 5:
        try:
            type = int(input(
                "Введите 1 - 3, чтобы выбрать метод прямоугольников(Л-1, П-2, С-3), 4 чтобы выбрать метод трапеций, "
                "5 чтобы выбрать метод Симпсона: "))
        except ValueError:
            print("Введите 1, 2, 3, 4 или 5 :")
    return type


def ask_error():
    err = 0
    while True:
        try:
            err = float(input("Введите точность: "))
            if err <= 0:
                print("число должно быть больше нуля")
                continue
            break
        except Exception:
            print("Введите число")
    return err


def ask_count_split():
    while True:
        try:
            n = int(input("Введите начальное целое число разбиения интервала интегрирования: "))
            if n > 0:
                return n
                break
            print("Число должно быть больше нуля")
        except ValueError:
            print("Введите целое число")
