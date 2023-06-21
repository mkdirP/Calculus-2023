from reader import Reader
from interpolator import Interpolator
from sympy import lambdify, sympify
from sympy import Symbol
from prettytable import PrettyTable, ALL
from numpy import isreal, isinf, isnan, isneginf
import warnings


def list_init(reader: Reader):
    reader.print_question("Откуда взять значения:\n(1) Набор точек\n(2) Функция")
    answer = reader.read_answer(["1", "2"], "Введите 1 или 2:", reader.is_contains_options)
    x_list, y_list = [], []
    eq = None

    if answer == "1":
        reader.print_question("Введите значения точек по x:")
        x_str = reader.read_answer([], "Все значения должны быть типа float. Попробуйте снова:", reader.is_float_list)
        x_list = list(map(float, x_str.split()))
        reader.print_question("Введите значения точек по y:")
        y_str = reader.read_answer([], "Все значения должны быть типа float. Попробуйте снова:", reader.is_float_list)
        y_list = list(map(float, y_str.split()))
    else:
        reader.print_question("Введите уравнение:")
        eq = reader.read_answer([], "Введите уравнение (с одной переменной):", reader.is_eq)
        eq = sympify(eq)
        eq = lambdify(Symbol('x'), eq)

        reader.print_question("Введите левый интервал:")
        left = float(reader.read_answer([], "Введите одно число:", reader.is_float))
        reader.print_question("Введите правый интервал:")
        right = float(reader.read_answer([], "Введите одно число:", reader.is_float))

        left = min(left, right)
        right = max(left, right)

        reader.print_question("Введите количество узлов интерполяции:")
        dot_count = int(reader.read_answer([2, 20, int], "Введите число, в интервале [2;20]:", reader.is_in_range))

        step = (right - left) / (dot_count - 1)
        for n in range(dot_count):
            try:
                x = left + step * n
                y = eq(x)

                if not isreal(x) or isnan(x) or isinf(x) or isneginf(x):
                    continue
                if not isreal(y) or isnan(y) or isinf(y) or isneginf(y):
                    continue

                x_list.append(x)
                y_list.append(y)
            except TypeError:
                continue

    if not x_list:
        x_list = [0]
        y_list = [0]

    left = min(x_list)
    right = max(x_list)
    reader.print_question("Введите точку x0:")
    x0 = float(
        reader.read_answer([left, right, float], f"Введите число, в интервале [{left};{right}]:", reader.is_in_range))

    return x_list, y_list, x0, eq


def to_fixed(num, digits):
    try:
        if round(float(num), digits) == 0:
            num = 0
        return f"{num:.{digits}f}"
    except ValueError:
        return str(num)


def print_differences(differences):
    table = PrettyTable()
    table.field_names = ["xᵢ", "yᵢ"] + [f"∆^{i} yᵢ" for i in range(1, len(differences))]
    for row in differences:
        table.add_row([to_fixed(elem, digits) for elem in row])
    print("Конечные разности:")
    print(table.get_string(header=True))


def print_dots(x_list, y_list):
    table = PrettyTable()
    table.hrules = ALL
    table.add_row(["x"] + [to_fixed(x, digits) for x in x_list])
    table.add_row(["y"] + [to_fixed(y, digits) for y in y_list])
    print("Полученные точки:")
    print(table.get_string(header=False))


warnings.filterwarnings("ignore")
while True:
    digits = 4
    reader = Reader()
    interpolator = Interpolator()

    x_list, y_list, x0, eq = list_init(reader)
    print()
    print_dots(x_list, y_list)
    print()

    differences = interpolator.finite_differences(x_list, y_list)
    print_differences(differences)
    print()

    if eq:
        print(f"Реальное значение: {to_fixed(eq(x0), digits)}")

    lagrange_result = interpolator.lagrange_method(x_list, y_list, x0)
    print(f"Многочлен Лагранжа: {to_fixed(lagrange_result, digits)}")

    gauss_result = interpolator.gauss_method(x_list, differences, x0)
    print(f"Многочлен Гаусса: {to_fixed(gauss_result, digits)}")

    interpolator.show_graph(x_list, y_list, differences, x0, [lagrange_result, gauss_result], eq)

    reader.print_question("")
    reader.print_question("Продолжить:\n(1) Да\n(2) Нет")
    answer = reader.read_answer(["1", "2"], "Введите 1 или 2:", reader.is_contains_options)
    if answer == "2":
        break
