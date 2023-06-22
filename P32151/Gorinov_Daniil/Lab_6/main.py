import numpy as np
import matplotlib.pyplot as plt
from math import exp


def euler_method(f, a, b, y0, h):
    dots = [(a, y0)]
    n = int((b - a) / h)
    for i in range(1, n + 1):
        dots.append((dots[i - 1][0] + h, dots[i - 1][1] + h * f(*dots[i - 1])))
    return dots


def fourth_order_runge_kutta(f, a, b, y0, h):
    dots = [(a, y0)]
    n = int((b - a) / h) + 1
    for i in range(1, n + 1):
        x_prev, y_prev = dots[i - 1]
        k1 = h * f(x_prev, y_prev)
        k2 = h * f(x_prev + h / 2, y_prev + k1 / 2)
        k3 = h * f(x_prev + h / 2, y_prev + k2 / 2)
        k4 = h * f(x_prev + h, y_prev + k3)
        x_cur = x_prev + h
        y_cur = y_prev + (k1 + 2 * k2 + 2 * k3 + k4) / 6
        dots.append((x_cur, y_cur))
    return dots


def milna_method(f, a, b, y0, h):
    dots = [(a, y0)]
    fun_t = [f(a, y0)]
    n = int((b - a) / h) + 1
    for i in range(1, 4):
        x_prev, y_prev = dots[i - 1]
        k1 = h * f(x_prev, y_prev)
        k2 = h * f(x_prev + h / 2, y_prev + k1 / 2)
        k3 = h * f(x_prev + h / 2, y_prev + k2 / 2)
        k4 = h * f(x_prev + h, y_prev + k3)
        x_cur = x_prev + h
        y_cur = y_prev + (k1 + 2 * k2 + 2 * k3 + k4) / 6
        dots.append((x_cur, y_cur))
        fun_t.append(f(x_cur, y_cur))
    for i in range(4, n):
        x_cur = dots[i - 1][0] + h
        y_pred = dots[i - 4][1] + 4 * h / 3 * (2 * fun_t[i - 3] - fun_t[i - 2] + 2 * fun_t[i - 1])
        fun_t.append(f(x_cur, y_pred))
        y_cor = dots[i - 2][1] + h / 3 * (fun_t[i - 2] + 4 * fun_t[i - 1] + fun_t[i])
        while 0.00001 < abs(y_cor - y_pred) / 29:
            y_pred = y_cor
            fun_t[i] = f(x_cur, y_pred)
            y_cor = dots[i - 2][1] + h / 3 * (fun_t[i - 2] + 4 * fun_t[i - 1] + fun_t[i])
        dots.append((x_cur, y_cor))
    return dots


def plot(x, y, acc_x, acc_y):
    plt.gcf().canvas.manager.set_window_title("График")
    ax = plt.gca()
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.plot(1, 0, marker=">", ms=5, color='k', transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot(0, 1, marker="^", ms=5, color='k', transform=ax.get_xaxis_transform(), clip_on=False)
    plt.plot(x, y, label="y(x)")
    plt.plot(acc_x, acc_y, label="acc_y(x)")
    plt.legend()
    plt.show(block=False)


def gettask(task_id):
    if task_id == '1':
        return lambda x, y: y + (1 + x) * (y ** 2), lambda x: -1 / x, 1, 1.5, -1
    elif task_id == '2':
        return lambda x, y: (x ** 2) - 2 * y, lambda x: 0.75 * exp(-2 * x) + 0.5 * (x ** 2) - 0.5 * x + 0.25, 0, 1, 1
    elif task_id == '3':
        return lambda x, y: (exp(2 * x) + y), lambda x: exp(2 * x), 0, 1, 1
    else:
        return None


def getdata_input():
    data = {}
    print("\nВыберите метод дифференцирования.")
    print(" 1 — Метод Эйлера")
    print(" 2 — Метод Рунге-Кутта 4-го порядка")
    print(" 3 — Метод Милна")
    while True:
        method_id = input("Метод дифференцирования: ")
        if method_id in ('1', '2', '3'):
            break
        print("Метода нет в списке!")
    data['method_id'] = method_id
    print("\nВыберите задачу.")
    print(" 1 — y' = y + (1 + x)y²\n     на [1; 1,5] при y(1) = -1")
    print(" 2 — y' = x² - 2y\n     на [0; 1] при y(0) = 1")
    print(" 3 — y' = e²ˣ + y\n     на [0; 0.25] при y(0) = 1")
    while True:
        task_id = input("Задача: ")
        func, acc_func, a, b, y0 = gettask(task_id)
        if func is not None:
            break
        print("Функции нет в списке!")
    data['f'] = func
    data['acc_f'] = acc_func
    data['a'] = a
    data['b'] = b
    data['y0'] = y0
    while True:
        try:
            h = float(input("\nВведите шаг точек: "))
            if h <= 0:
                raise ValueError
            break
        except ValueError:
            print("Шаг точек должен быть положительным числом.")
    data['h'] = h
    return data


if __name__ == '__main__':
    print("\033[93m{}\033[0m".format("Лабораторная работа #6\nГоринов Даниил Андреевич\nВариант 3"))
    data = getdata_input()
    if data['method_id'] == '1':
        answer = euler_method(data['f'], data['a'], data['b'], data['y0'], data['h'])
    elif data['method_id'] == '2':
        answer = fourth_order_runge_kutta(data['f'], data['a'], data['b'], data['y0'], data['h'])
    elif data['method_id'] == '3':
        answer = milna_method(data['f'], data['a'], data['b'], data['y0'], data['h'])
    else:
        answer = None
    if answer is None:
        print("\n\nВо время вычисления произошла ошибка!")
    else:
        x = np.array([dot[0] for dot in answer])
        y = np.array([dot[1] for dot in answer])
        acc_x = np.linspace(np.min(x), np.max(x), 100)
        acc_y = [data['acc_f'](i) for i in acc_x]
        plt.plot(x, y, acc_x, acc_y)

        print("\n\nРезультаты вычисления.")
        print("%12s%12s%12s" % ("x", "y", "acc_y"))
        for i in range(len(answer)):
            print("%12.4f%12.4f%12.4f" % (answer[i][0], answer[i][1], data['acc_f'](answer[i][0])))
        plt.show()
