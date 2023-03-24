import typing
from typing import Callable
import numpy as np
import matplotlib.pyplot as plt
from sympy import *
from sympy.plotting.plot import MatplotlibBackend
from methods_equations import x, available_functions, chord_method, secant_method, SimpleIterationException, simple_iteration
from methods_systems import available_systems, newton_method, y
from os import getcwd


def get_function_by_number(number: int) -> Add:
    index = number - 1
    if index < 0 or index >= len(available_functions):
        raise ValueError
    return available_functions[index]


def get_system_by_number(number: int) -> typing.Tuple[Add, Add]:
    index = number - 1
    if index < 0 or index >= len(available_systems):
        raise ValueError
    return available_systems[index]


def print_all_functions():
    for index, function_string in enumerate(available_functions):
        print(f"{index+1}: {function_string}")


def print_all_systems():
    for index, system in enumerate(available_systems):
        print(f"System #{index + 1}")
        for equation in system:
            print(equation)
        print()


# Plots a function on an interval
def plot_function(a: int, b: int, function: Callable[[float], float], solution: typing.Tuple[float, float]) -> None:
    x_vals = np.linspace(a - 2, b + 2, 1000)
    y_vals = list(map(function, x_vals))
    plt.plot(x_vals, y_vals, )
    plt.xlabel("x - axis")
    plt.ylabel("y - axis")
    plt.scatter([solution[0]], solution[1], color="red")
    plt.show()


def plot_system(system: typing.Tuple[Add, Add], solution: typing.Tuple[float, float]) -> None:
    p1 = plot_implicit(Eq(system[0], 0), x_var=x, y_var=y, show=False)
    p2 = plot_implicit(Eq(system[1], 0), x_var=x, y_var=y, line_color="Red", show=False)
    p1.append(p2[0])
    backend = MatplotlibBackend(p1)
    backend.process_series()
    backend.fig.tight_layout()
    plt = backend.plt
    plt.scatter([solution[0]], [solution[1]], color="Green")
    plt.show()


def get_error_length(eps: float):
    if "e" in str(eps):
        return abs(int(str(eps).split("e")[1]))
    return len(str(eps).split(".")[1])


def print_results(results: typing.Tuple[float, float, int], epsilon, file_flag=False, file_name=None):
    error_length =get_error_length(epsilon)
    output = f"Method finished in {results[2]} iterations." + "\n" + \
             f"Result value is: {round(results[0], error_length)}." + "\n" +\
             f"Function value of result: {round(results[1], error_length+3)}"
    if file_flag:
        with open(getcwd() + '/' + file_name, "w") as file:
            file.writelines(output)
    else:
        print(output)


def print_system_results(results: typing.Tuple[typing.Tuple[float, float], int, typing.Tuple[float, float], typing.Tuple[float, float]], epsilon: float):
    error_length = get_error_length(epsilon)
    answers = results[0]
    errors = results[2]
    equations = results[3]
    print(f"Results are: x = {round(answers[0], error_length)}, y = {round(answers[1], error_length)}")
    print(f"Number of iterations: {results[1]}")
    print(f"Errors vector: error_x = {round(errors[0], error_length + 3)}, error_y = {round(errors[1], error_length + 3)}")
    print(f"Equations value with result x, y: f = {round(equations[0], error_length)}, g = {round(equations[1], error_length)}")


# Main function to communicate with user about nonlinear equations
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
        file_in_flag = input_stream_id == 1
        output_stream_id = int(input("Input:\n1 to output data to file\n2 to output to console\n"))
        file_out_flag = output_stream_id == 1
    except ValueError:
        print("Wrong number")
        return
    if not file_in_flag:
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
        output_filename = None
        if file_out_flag:
            output_filename = input("Input output filename: ")
        results = method(a, b, epsilon, func)
        plot_function(a, b, lambdify(x, func, 'numpy'), tuple([results[0], lambdify(x, func, 'numpy')(results[0])]))
        print_results(results, epsilon, file_out_flag, output_filename)
    except ValueError:
        print("Incorrect interval")
    except SimpleIterationException:
        print("Can not build proper iteration function")
    except FileNotFoundError:
        print("Output file does not exist")


def system_of_equations():
    print_all_systems()
    try:
        system_number = int(input("Input system number: "))
        system = get_system_by_number(system_number)
        x_0, y_0 = [float(i) for i in input("Input initial values for x and y with space between them, for example, 2.1 4\n").split()]
        epsilon = float(input("Input allowed error: "))
        results = newton_method(x_0, y_0, epsilon, system)
        print_system_results(results, epsilon)
        plot_system(system, results[0])
    except ValueError:
        print("Wrong number")
        return


# Main function to communicate with user
if __name__ == "__main__":
    try:
        n = int(input("Input:\n1 to solve nonlinear equation\n2 to solve system of nonlinear equations\n"))
        if n > 2 or n < 1:
            raise ValueError
    except ValueError:
        print("Incorrect data")
        exit(0)
    if n == 1:
        nonlinear_equation_main()
    elif n == 2:
        system_of_equations()
