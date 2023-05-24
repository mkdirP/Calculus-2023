from sympy import Add, lambdify
from methods import equations, get_current_solution, solve_single_turn, modified_euler, x, runge_kutt, adams, get_errors
from typing import List, Tuple
import matplotlib.pyplot as plt
import numpy as np
import warnings

warnings.filterwarnings("ignore")


def plot_exact_solution(partial_solution: Add, xs: List[float]):
    func = lambdify(x, partial_solution, 'numpy')
    new_xs = np.linspace(xs[0], xs[-1], 1000)
    ys = list(map(func, new_xs))
    plt.plot(new_xs, ys, label="Точное решение", color="red")
    plt.scatter(xs, list(map(func, xs)), color="red")


def plot_computed_solution(xs: List[float], ys: List[float], name: str):
    plt.plot(xs, ys, label=name)


def plot_all(solutions: List[Tuple[List[float], str]], partial_solution: Add, xs: List[float]):
    plot_exact_solution(partial_solution, xs)
    for solution in solutions:
        plot_computed_solution(xs, solution[0], solution[1])
    plt.legend()
    plt.show()


def print_equations():
    for index, eq in enumerate(equations):
        print(f"{index+1}. y' = {eq}")


def get_epsilon_length(epsilon: float) -> int:
    if "e" in str(epsilon):
        return int(str(epsilon)[-1])
    return len(str(epsilon).split(".")[-1])


def round_list(l: List[float], epsilon: float) -> List[str]:
    round_length = get_epsilon_length(epsilon)
    return [str(round(i, round_length)) for i in l]


def print_single_turn_results(results: List[Tuple[List[float], str] | Tuple[List[float], str, float]], xs: List[int], epsilon: float):
    xs = round_list(xs, epsilon)
    for res in results:
        print(res[1])
        print(f"x     {' '.join(xs)}")
        print(f"y     {' '.join(round_list(res[0], epsilon))}")
        if len(res) == 3:
            print(f"error {' '.join(round_list([res[2]], epsilon))}")
        print()


def main():
    try:
        print_equations()
        eq_number = int(input("Введите номер уравнения: "))
        eq_number -= 1
        x_0, y_0 = map(float, input("Введите начальные условия x_0, y_0 через пробел: ").split())
        x_n = float(input("Введите конец интервала дифференцирования: "))
        if x_n < x_0:
            raise ValueError
        h = float(input("Введите шаг: "))
        epsilon = float(input("Введите точность: "))
        partial_solution = get_current_solution(eq_number, x_0, y_0)
        xs = [x_0]
        while abs(xs[-1] - x_n) > epsilon:
            xs.append(xs[-1] + h)

        solutions = []

        ys_modified_euler = solve_single_turn(modified_euler, eq_number, x_0, y_0, h, x_n, epsilon, 2)
        solutions.append((ys_modified_euler, "Модифицированный метод Эйлера"))

        ys_runge_kutt = solve_single_turn(runge_kutt, eq_number, x_0, y_0, h, x_n, epsilon, 4)
        solutions.append((ys_runge_kutt, "Метод Рунге-Кутта"))

        ys_adams = adams(eq_number, x_0, y_0, h, x_n, epsilon)
        errors = get_errors(ys_adams, list(map(lambdify(x, partial_solution, 'numpy'), xs)))
        solutions.append((ys_adams, "Метод Адамса", max(errors)))

        print_single_turn_results(solutions, xs, epsilon)

        plot_all(solutions, partial_solution, xs)
    except ValueError as e:
        print(e)
        print("Invalid input.")


if __name__ == "__main__":
    main()
