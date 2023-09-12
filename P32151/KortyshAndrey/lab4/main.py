from typing import Tuple, List
from functions import get_polynom, var, get_exponential, get_power,\
    get_logarithmic, get_extra_information, get_pirson_coefficient
import matplotlib.pyplot as plt
from sympy import Add, lambdify
import numpy as np
import warnings
warnings.filterwarnings("ignore")


def plot(x: List[float], y: List[float], functions: List[Add]) -> None:
    # Colors for functions
    colors = ["green", "blue", "yellow", "orange", "purple", "red"]

    # Plot initial points
    plt.scatter(x, y, color="red")

    # Plot functions
    x_vals = np.linspace(min(x) - 2, max(x) + 2, 1000)
    for index, func in enumerate(functions):
        y_vals = list(map(lambdify(var, func, "numpy"), x_vals))
        plt.plot(x_vals, y_vals, colors[index % len(colors)], label=str(func))
    plt.xlabel("x - axis")
    plt.ylabel("y - axis")
    plt.legend()
    plt.show()


def input_from_file(filename: str) -> Tuple[List[float], List[float]]:
    with open(filename, "r") as f:
        x = list(map(float, f.readline().split()))
        y = list(map(float, f.readline().split()))
    return x, y


def input_from_console() -> Tuple[List[float], List[float]]:
    x = list(map(float, input("Введите значения x через пробел:\n").split()))
    y = list(map(float, input("Введите значения y через пробел:\n").split()))
    return x, y


def join_list(l, precision=3):
    return " ".join(str(round(i, precision)) for i in l)


def output_results_console(x, y, results, precision=3) -> None:
    for index, (func, dev, phi, epsilon) in enumerate(results):
        print(f"Текущая функция:\n {func}")
        print(f"Среднеквадратичное отклонение:\n {round(dev, precision)}")
        print(f"Значения функции на текущих x:\n {join_list(phi, precision)}")
        print(f"Отклонение значений функции от реальных:\n {join_list(epsilon, precision)}")
        if index == 0:
            print(f"Коэффициент Пирсона равен: {round(get_pirson_coefficient(x, y), precision)}")
        print()
    print(f"Лучшая аппроксимирующая функция: {sorted(results, key=lambda x: x[1])[0][0]}")


def output_results_file(filename: str, x, y, results, precision=3) -> None:
    with open(filename, "w") as f:
        for index, (func, dev, phi, epsilon) in enumerate(results):
            f.write(f"Текущая функция:\n {func}\n")
            f.write(f"Среднеквадратичное отклонение:\n {round(dev, precision)}\n")
            f.write(f"Значения функции на текущих x:\n {join_list(phi, precision)}\n")
            f.write(f"Отклонение значений функции от реальных:\n {join_list(epsilon, precision)}\n")
            if index == 0:
                f.write(f"Коэффициент Пирсона равен: {round(get_pirson_coefficient(x, y), precision)}\n")
            f.write("\n")
    f.write(f"Лучшая аппроксимирующая функция: {sorted(results, key=lambda x: x[1])[0][0]}\n")


def main():
    precision = 3
    try:
        file_descriptor = int(input("Введите 0 для ввода из консоли, 1 для ввода из файла:\n"))
        if file_descriptor == 0:
            x, y = input_from_console()
        elif file_descriptor == 1:
            x, y = input_from_file(input("Введите имя файла:\n"))
        else:
            raise ValueError
        results = []
        for i in range(1, 4):
            try:
                func, dev = get_polynom(x, y, i, precision)
                phi, epsilon = get_extra_information(func, x, y)
                results.append((func, dev, phi, epsilon))
            except ZeroDivisionError as e:
                pass
        for func_to_call in [get_exponential, get_power, get_logarithmic]:
            try:
                func, dev = func_to_call(x, y, precision)
                phi, epsilon = get_extra_information(func, x, y)
                results.append((func, dev, phi, epsilon))
            except ZeroDivisionError as e:
                pass
            except ValueError as e:
                pass
        output_descriptor = int(input("Введите 0 для вывода результатов в консоль, 1 для вывода в файл:\n"))
        if output_descriptor == 0:
            output_results_console(x, y, results, precision)
        elif output_descriptor == 1:
            output_results_file(input("Введите имя файла:\n"), x, y, results, precision)
        else:
            raise ValueError
        plot(x, y, [i[0] for i in results])
    except ValueError as e:
        print("Неправильный ввод.")
    except FileNotFoundError as e:
        print("Неправильное имя файла.")


if __name__ == "__main__":
    main()
