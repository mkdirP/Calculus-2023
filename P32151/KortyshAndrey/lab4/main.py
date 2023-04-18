from typing import Tuple, List
from functions import get_polynom, var, get_exponential, get_power, get_logarithmic
import matplotlib.pyplot as plt
from sympy import Add, lambdify
import numpy as np


def plot(x: List[float], y: List[float], functions: List[Add]) -> None:
    # Colors for functions
    colors = ["green", "blue", "yellow", "orange", "purple", "red"]

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
        file_descriptor = int(input("Введите 0 для ввода из консоли, 1 для ввода из файла:\n"))
        if file_descriptor == 0:
            x, y = input_from_console()
        elif file_descriptor == 1:
            x, y = input_from_file(input("Введите имя файла:\n"))
        else:
            raise ValueError
        results = []
        for i in range(1, 4):
            func, dev = get_polynom(x, y, i)
            results.append((func, dev))
        results.append(get_exponential(x, y))
        results.append(get_power(x, y))
        results.append(get_logarithmic(x, y))
        print([i[0] for i in results])
        plot(x, y, [i[0] for i in results])
    except ValueError as e:
        print("Неправильный ввод.")


if __name__ == "__main__":
    main()
