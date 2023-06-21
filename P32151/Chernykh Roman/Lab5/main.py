from calculations import *
from dataProcessing import *
import numpy as np


def funct(num):
    if num == 1:
        return lambda x: np.sin(x)
    if num == 2:
        return lambda x: x**2 + 7
    if num == 3:
        return lambda x: x**3+16


if ask_input_data() == 1:
    x, y = get_points_file()
    temp_func = None
else:
    num = int(input("Введите номер желаемой функции:\n 1) sin(x)\n 2) x^2 + 7\n 3) x^3 + 16\n "))
    func = funct(num)
    print("Введите границы интервала для набора точек")
    a, b = ask_num(), ask_num()
    if a > b:
        a, b = b, a
    step = 0
    print("Введите шаг: ")
    while step <= 0:
        step = ask_num()
    x, y = get_points_from_func(func, a, b, step)
    temp_func = func

x_plot = np.linspace(np.min(x) - plot_area, np.max(x) + plot_area, 1000)
plot_lag_newton(x_plot, temp_func,
                [lagrange_method(x, y, x_now) for x_now in x_plot],
                [newton_method(x, y, x_now) for x_now in x_plot],
                [stirling_method(x, y, x_now) for x_now in x_plot],
                [bessel_method(x, y, x_now) for x_now in x_plot], x, y)
while True:
    print("Введите X: ")
    n = ask_num()
    print("Методом Лагранжа: ", lagrange_method(x, y, n))
    print("Методом Ньютона: ", newton_method(x, y, n))
    print("Методом Стирлинга: ", stirling_method(x, y, n))
    print("Методом Бесселя: ", bessel_method(x, y, n))
    print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
