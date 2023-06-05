import numpy as np
import matplotlib.pyplot as plt
from itertools import groupby
from calc import *
from io import *

plot_offset = 2
INPUT = "./input.txt"


def draw_plot(x, f_y, lag_y, newton_y, stirling_y, bessel_y, point_x, point_y):
    if f_y is not None:
        plt.plot(x, f_y(x), linewidth=2.0, label="function")
    plt.plot(x, lag_y, linewidth=2.0, label="lagrange")
    plt.plot(x, newton_y, linewidth=2.0, label="newton")
    plt.plot(x, stirling_y, linewidth=2.0, label="stirling")
    plt.plot(x, bessel_y, linewidth=2.0, label="bessel")
    plt.plot(point_x, point_y, '*', linewidth=0, label="points")
    plt.legend()
    plt.grid(True)
    minimum_x = min(point_x)
    minimum_y = min(point_y)
    maximum_x = max(point_x)
    maximum_y = max(point_y)
    plt.xlim(minimum_x - plot_offset, maximum_x + plot_offset)
    plt.ylim(minimum_y - plot_offset, maximum_y + plot_offset)
    plt.show()


def sort_and_delete_dublicates(points):
    points.sort()
    i = 1
    while i < len(points):
        if points[i][0] == points[i - 1][0]:
            points[i - 1] = (points[i - 1][0], (points[i - 1][1] + points[i][1]) / 2)
            points.pop(i)
        else:
            i += 1
    return points

def get_points_file():
    # Получение точек из файла
    with open(INPUT, 'rt') as file:
        try:
            x = []
            y = []
            for line in file:
                new_row = list(map(float, line.strip().split()))
                if len(new_row) != 2:
                    raise ValueError
                x.append(new_row[0])
                y.append(new_row[1])
            t = [(x[i], y[i]) for i in range(len(x))]
            p = sort_and_delete_dublicates(t)
            x = [p[0] for p in t]
            y = [p[1] for p in t]
        except ValueError:
            print("Неверный формат файла")
            exit()
    return x, y


def ask_input_data():
    mode = 0
    while mode != 1 and mode != 2:
        try:
            mode = int(input("Ведите источник данных. Для файла - 1, из функции - 2: "))
        except Exception:
            print("Введите число")
    return mode


def choose_func():
    func = 0
    while True:
        try:
            print("Функции: \n 1) sin(x)\n 2) x^2 \n 3) x^3")
            func = int(input("Выберите функцию (укажите номер): "))
        except Exception:
            print("Введите ЦЕЛОЕ ЧИСЛО 1, 2 или 3!")
        if func in range(1, 4):
            return func
        print("Выберите одно целое число 1, 2 или 3")


def chosen_func():
    fun_haha = choose_func()
    if fun_haha == 1:
        return lambda f: np.sin(f)
    if fun_haha == 2:
        return lambda f: f ** 2
    if fun_haha == 3:
        return lambda f: f ** 3


# main part
print("\033[31m\033[40m{}".format("Soloviev Artemiy P32151"))
print("Task option 8")
print("\033[0m".format())
if ask_input_data() == 1:
    x, y = get_points_file()
    temp_func = None
else:
    func = chosen_func()
    while True:
        try:
            print("Введите границы интервала для набора точек")
            a = float(input("Введите левую границу: "))
            b = float(input("Введите правую границу: "))
            if a > b:
                print("Вы ввели наоборот, но я это предусмотрел")
                a, b = b, a
            break
        except Exception:
            print("Введите число!!!")
    while True:
        try:
            st = float(input("Введите шаг: "))
            if (st < 0):
                print("Шагаем только вперед и только вперед!!")
            elif st == 0:
                print("Шагаем, а не стоим!!")
            else:
                break
        except:
            print("Нужно ввести число...")
    x, y = get_points_from_func(func, a, b, st)
    temp_func = func

x_plot = np.linspace(np.min(x) - plot_offset, np.max(x) + plot_offset, 1000)
draw_plot(x_plot, temp_func,
          [lagrange_method(x, y, x_now) for x_now in x_plot],
          [newton_method(x, y, x_now) for x_now in x_plot],
          [stirling_method(x, y, x_now) for x_now in x_plot],
          [bessel_method(x, y, x_now) for x_now in x_plot], x, y)
while True:
    while True:
        try:
            n = input("Введите Х: ")
            if n == "X" or n == "Х" or n == "x" or n == "х":
                print("ха-ха очень смешно...")
            n = float(n)
            break
        except Exception:
            print("X должен быть числом")
    print("Метод Лагранжа: ", lagrange_method(x, y, n))
    print("Метод Ньютона: ", newton_method(x, y, n))
    print("\033[32m{}".format("*вау это что доп.задание????*"), "\033[0m".format())
    print("Метод Бесселя: ", bessel_method(x, y, n))
    print("Метод Стирлинга: ", stirling_method(x, y, n))
    print("----------------------------------------------------------")
