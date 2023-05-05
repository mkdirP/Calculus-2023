from typing import List, Tuple
from sympy import Add, lambdify
import matplotlib.pyplot as plt
import numpy as np
from methods import get_finite_differences, get_lagrange_polynom, var, get_gauss_polynom, get_stirling_polynom,\
    get_bessel_polynom, functions
import warnings


warnings.filterwarnings("ignore")


def plot_results(results: List[Tuple[Add, float, str]], x: List[float], y: List[float], x_ans: float) -> None:
    plt.plot(x, y, color="black")
    plt.scatter(x, y, color="red")
    colors = ["blue", "orange", "yellow", "green"]
    # plt.scatter([x_ans], [results[1][1]], color="green", label="gauss interpolation")
    for index, result in enumerate(results):
        xs = np.linspace(min(x), max(x), 1000)
        ys = list(map(lambdify(var, result[0], "numpy"), xs))
        plt.plot(xs, ys, color=colors[index])
        plt.scatter([x_ans], [result[1]], label=result[2], color=colors[index])
    plt.legend()
    plt.show()


def print_finite_differences(diff: List[List[float]], precision=3) -> None:
    header = ["y_i", "Δy_i"]
    for i in range(2, len(diff)):
        header.append(f"Δ^{i}y_i")
    print((precision*" ").join(header))
    for row in diff:
        print((precision*" ").join(str(round(i, precision)) for i in row))


def print_results(results: List[Tuple[Add, float, str]], precision=3) -> None:
    for result in results:
        print(f"Результат {result[2]}: {round(result[1], precision)}")


def print_functions():
    for index, func in enumerate(functions):
        print(f"{index}. {func}")


def get_x_y_from_function(func: Add, a: int, b: int, n: int) -> Tuple[List[float], List[float]]:
    x = list(np.linspace(a, b, n))
    y = list(map(lambdify(var, func, "numpy"), x))
    return x, y


def main():
    precision = 4
    try:
        # input
        choice = int(input("Введите 0 для ввода из консоли, 1 для ввода из файла, 2 для выбора функции:\n"))
        if choice < 0 or choice > 2:
            raise ValueError
        if choice == 0:
            x = [float(i) for i in input("Введите значения x через пробел:\n").split()]
            y = [float(i) for i in input("Введите значения y через пробел:\n").split()]
        elif choice == 1:
            with open(input("Введите имя файла:\n"), "r") as f:
                x = list(map(float, f.readline().split()))
                y = list(map(float, f.readline().split()))
        elif choice == 2:
            print_functions()
            index = int(input("Введите индекс функции:\n"))
            if index < 0 or index >= len(functions):
                raise ValueError
            cur_function = functions[index]
            a, b = [int(i) for i in input("Введите концы интервала через пробел:\n").split()]
            n = int(input("Введите количество промежутков:\n"))
            if n <= 0:
                raise ValueError
            x, y = get_x_y_from_function(cur_function, a, b, n)

        x_ans = float(input("Введите интересующее вас значение аргумента:\n"))

        if len(x) != len(y):
            raise ValueError
        if len(x) < 2:
            raise ValueError
        if len(set(x)) != len(x):
            raise ValueError

        dict_x_to_y = {x_i: y_i for x_i, y_i in zip(x, y)}
        x.sort()
        y = [dict_x_to_y[x_i] for x_i in x]

        # input over

        # pretty self-explanatory
        differences = get_finite_differences(y)
        print_finite_differences(differences, precision)

        # calculate
        results = []

        lagrange_polynom, y_ans_lagrange = get_lagrange_polynom(x, y, x_ans)
        results.append((lagrange_polynom, y_ans_lagrange, "метода Лагранжа"))

        gauss_polynom, y_ans_gauss = get_gauss_polynom(x, y, x_ans)
        results.append((gauss_polynom, y_ans_gauss, "метода Гаусса"))

        stirling_polynom, y_ans_stirling = get_stirling_polynom(x, y, x_ans)
        results.append((stirling_polynom, y_ans_stirling, "метода Стирлинга"))

        bessel_polynom, y_ans_bessel = get_bessel_polynom(x, y, x_ans)
        results.append((bessel_polynom, y_ans_bessel, "метода Бесселя"))

        plot_results(results, x, y, x_ans)
        print_results(results, precision)

    except ValueError as e:
        print("Некорректные данные")
    except FileNotFoundError as e:
        print("Нет такого файла")


if __name__ == "__main__":
    main()
