import typing
from typing import Callable
import numpy as np
import matplotlib.pyplot as plt
from sympy import *
from methods_equations import x, available_functions, chord_method, secant_method, SimpleIterationException, simple_iteration
from os import getcwd


def get_function_by_number(number: int) -> Add:
    index = number - 1
    if index < 0 or index >= len(available_functions):
        raise ValueError
    return available_functions[index]


def print_all_functions():
    for index, function_string in enumerate(available_functions):
        print(f"{index+1}: {function_string}")


# Plots a function on an interval
def plot_function(a: int, b: int, function: Callable[[float], float]) -> None:
    x_vals = np.linspace(a - 2, b + 2, 1000)
    y_vals = list(map(function, x_vals))
    plt.plot(x_vals, y_vals)
    plt.xlabel("x - axis")
    plt.ylabel("y - axis")
    plt.show()


def print_results(results: typing.Tuple[float, float, int], epsilon):
    error_length = len(str(epsilon).split(".")[1])
    print(f"Method finished in {results[2]} iterations.")
    print(f"Result value is: {round(results[0], error_length)}.")
    print(f"Function value of result: {round(results[1], error_length+3)}")


# Main function to communicate with user
def nonlinear_equation_main():
    try:
        print_all_functions()
        function_number = int(input("Input function number: "))
        func = get_function_by_number(function_number)
    except ValueError:
        print("Incorrect function number")
        return
    try:
        input_stream_id = int(input("Input:\n1 to get data interval and error from file\n2 to proceed via console\n"))
        if input_stream_id > 2 or input_stream_id < 1:
            raise ValueError
        file_flag = input_stream_id == 1
    except ValueError:
        print("Wrong number")
        return
    if not file_flag:
        try:
            a, b = [float(i) for i in input("Input interval start and end with space between them, for example, 2.1 4:\n").split()]
            epsilon = float(input("Input allowed error: "))
        except ValueError:
            print("Incorrect input data")
            return
        print("Available method names are:\n1. Chord\n2. Secant\n3. Iteration")
        method_name = input("Input method name: ")
    else:
        filename = input("Input filename: ")
        try:
            with open(getcwd() + '/' + filename, "r") as file:
                a, b = [float(i) for i in file.readline().split()]
                epsilon = float(file.readline())
                method_name = file.readline().strip()
        except ValueError as e:
            print("Incorrect data in file")
            return
        except FileNotFoundError:
            print("No such file")
            return
    plot_function(a, b, lambdify(x, func, 'numpy'))
    if method_name == "Chord":
        method = chord_method
    elif method_name == "Secant":
        method = secant_method
    elif method_name == "Iteration":
        method = simple_iteration
    else:
        print("No such method.")
        return
    try:
        print_results(method(a, b, epsilon, func), epsilon)
    except ValueError:
        print("Incorrect interval")
    except SimpleIterationException:
        print("Can not build proper iteration function")


if __name__ == "__main__":
    nonlinear_equation_main()
