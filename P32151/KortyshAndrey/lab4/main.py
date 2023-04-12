from typing import Tuple, List
from functions import get_linear, var
import matplotlib.pyplot as plt
from sympy import Add, lambdify
import numpy as np


def plot(x: List[float], y: List[float], functions: List[Add]) -> None:
    # Colors for functions
    colors = ["green", "blue", "yellow"]

    # Plot initial points
    plt.scatter(x, y, color="red")

    # Plot functions
    x_vals = np.linspace(min(x) - 2, max(x) + 2, 1000)
    for index, func in enumerate(functions):
        y_vals = list(map(lambdify(var, func, "numpy"), x_vals))
        plt.plot(x_vals, y_vals, colors[index % len(colors)])
    plt.xlabel("x - axis")
    plt.ylabel("y - axis")
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


def main():
    try:
        functions = []
        file_descriptor = int(input("Введите 0 для ввода из консоли, 1 для ввода из файла:\n"))
        if file_descriptor == 0:
            x, y = input_from_console()
        elif file_descriptor == 1:
            x, y = input_from_file(input("Введите имя файла:\n"))
        else:
            raise ValueError
        linear_func, linear_dev = get_linear(x, y)
        functions.append(linear_func)


        plot(x, y, functions)
    except ValueError:
        print("Неправильный ввод.")


if __name__ == "__main__":
    main()
