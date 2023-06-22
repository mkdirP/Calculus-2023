import time

import numpy as np
import matplotlib.pyplot as plt


def lagrange_polynomial(dots, x):
    result = 0
    n = len(dots)
    for i in range(n):
        c1 = c2 = 1
        for j in range(n):
            if i != j:
                c1 *= x - dots[j][0]
                c2 *= dots[i][0] - dots[j][0]
        result += dots[i][1] * c1 / c2
    return result


def newton_polynomial(dots, x):
    y_arr = [i[1] for i in dots]
    x_arr = [i[0] for i in dots]
    diff = [y_arr]
    for i in range(len(x_arr)):
        tmp_dif = []
        for j in range(len(x_arr) - i - 1):
            tmp_dif.append((diff[-1][j + 1] - diff[-1][j]) / (x_arr[j + i + 1] - x_arr[j]))

        diff.append(tmp_dif)
    mul = 1
    answer = y_arr[0]
    for i in range(len(x_arr) - 1):
        mul *= (x - x_arr[i])
        answer += diff[i + 1][0] * mul
    return answer


def sterling_scheme(dots, x):
    n = len(dots)

    def divided_differences(dots):
        n = len(dots)
        divided_diff = [[y for _, y in dots]]
        for i in range(1, n):
            diff = [(divided_diff[i - 1][j + 1] - divided_diff[i - 1][j]) / (dots[j + i][0] - dots[j][0]) for j in
                    range(n - i)]
            divided_diff.append(diff)
        return divided_diff

    def sterling_polynomial(dots, divided_diff, x):
        n = len(dots)
        y = divided_diff[0][0]
        p = 1
        for i in range(1, n):
            p *= (x - dots[i - 1][0])
            y += divided_diff[i][0] * p
        return y
    divided_diff = divided_differences(dots)
    result = sterling_polynomial(dots, divided_diff, x)
    return result


def bessel_scheme(dots, x):
    n = len(dots)
    result = 0.0
    for i in range(n):
        term = dots[i][1]
        for j in range(n):
            if i != j:
                term *= (x - dots[j][0]) / (dots[i][0] - dots[j][0])
        result += term
    return result


def plot(x, y, plot_x, plot_y):
    plt.gcf().canvas.manager.set_window_title("График")
    ax = plt.gca()
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.plot(1, 0, marker=">", ms=5, color='k', transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot(0, 1, marker="^", ms=5, color='k', transform=ax.get_xaxis_transform(), clip_on=False)
    plt.plot(x, y, 'o', plot_x, plot_y)
    plt.show(block=False)


def getfunc(func_id):
    if func_id == '1':
        return lambda x: np.sqrt(x)
    elif func_id == '2':
        return lambda x: x ** 2
    elif func_id == '3':
        return lambda x: np.sin(x)
    else:
        return None


def make_dots(f, a, b, n):
    dots = []
    h = (b - a) / (n - 1)
    for i in range(n):
        dots.append((a, f(a)))
        a += h
    return dots


def getdata_input():
    data = {}
    print("\nВыберите метод интерполяции.")
    print(" 1 — Многочлен Лагранжа")
    print(" 2 — Многочлен Ньютона с конечными разностями")
    print(" 3 — Схема Стирлинга")
    print(" 4 — Схема Бесселя")
    while True:
        method_id = input("Метод решения: ")

        if method_id in ['1', '2', '3', '4']:
            break
        else:
            print("Метода нет в списке.")
    data['method_id'] = method_id
    print("\nВыберите способ ввода исходных данных.")
    print(" 1 — Набор точек")
    print(" 2 — Функция")
    while True:
        input_method_id = input("Способ: ")
        if input_method_id in ['1', '2']:
            break
        else:
            print("Способа нет в списке.")
    dots = []
    if input_method_id == '1':
        print("Вводите координаты через пробел, каждая точка с новой строки.")
        print("Чтобы закончить, введите 'END'.")
        while True:
            current = input()
            if current == 'END':
                if len(dots) < 2:
                    print("Минимальное количество точек - две!")
                break
            try:
                x, y = map(float, current.split())
                for dot in dots:
                    if x in dot:
                        x += 0.001
                dots.append((x, y))
            except ValueError:
                print("Введите точку повторно - координаты должны быть числами!")
    elif input_method_id == '2':
        print("\nВыберите функцию.")
        print(" 1 — √x")
        print(" 2 - x²")
        print(" 3 — sin(x)")
        while True:
            func_id = input("Функция: ")
            func = getfunc(func_id)
            if func is not None:
                break
            else:
                print("Функции нет в списке.")
        print("\nВведите границы отрезка.")
        while True:
            try:
                a, b = map(float, input("Границы отрезка: ").split())
                if func_id == '1':
                    a = max(0.0, a)
                    b = max(0.0, b)
                if a > b:
                    a, b = b, a
                break
            except ValueError:
                print("Границы отрезка должны быть числами, введенными через пробел.")
        print("\nВыберите количество узлов интерполяции.")
        while True:
            try:
                n = int(input("Количество узлов: "))
                if n < 2:
                    raise ValueError
                break
            except ValueError:
                print("Количество узлов должно быть целым числом > 1.")
        dots = make_dots(func, a, b, n)
    data['dots'] = dots
    print("\nВведите значение аргумента для интерполирования.")
    while True:
        try:
            x = float(input("Значение аргумента: "))
            break
        except ValueError:
            print("Значение аргумента должно быть числом.")
    data['x'] = x
    return data


if __name__ == '__main__':
    print("\033[93m{}\033[0m".format("Лабораторная работа #5\n"
                                     "Горинов Даниил Андреевич\n"
                                     "Вариант 3"))
    data = getdata_input()
    x = np.array([dot[0] for dot in data['dots']])
    y = np.array([dot[1] for dot in data['dots']])
    plot_x = np.linspace(np.min(x), np.max(x), 100)
    plot_y = None
    if data['method_id'] == '1':
        answer = lagrange_polynomial(data['dots'], data['x'])
        plot_y = [lagrange_polynomial(data['dots'], x) for x in plot_x]
    elif data['method_id'] == '2':
        answer = newton_polynomial(data['dots'], data['x'])
        plot_y = [newton_polynomial(data['dots'], x) for x in plot_x]
    elif data['method_id'] == '3':
        answer = sterling_scheme(data['dots'], data['x'])
        plot_y = [sterling_scheme(data['dots'], x) for x in plot_x]
    elif data['method_id'] == '4':
        answer = bessel_scheme(data['dots'], data['x'])
        plot_y = [bessel_scheme(data['dots'], x) for x in plot_x]
    else:
        answer = None
    if answer is not None:
        plt.plot(x, y, plot_x, plot_y)
    print("\n\nРезультаты вычисления.")
    print(f"Приближенное значение функции: {answer}")
    plt.show()