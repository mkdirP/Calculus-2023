import numpy as np
import matplotlib.pyplot as plt
from sympy import *

import input_data
from util import check_for_roots
from util import draw_graphic
from util import draw_graphic_for_systems
import methods

q, w = symbols('q w')

eq = {
    1: q ** 2 + w ** 2 - 4,
    2: w - 3 * q**2,
    3: 0.1 * q ** 2 + q + 0.2 * w ** 2 - 0.3,
    4: 0.2 * q ** 2 + w + 0.1 * q * w - 0.7,
}


method = input_data.choose_method()
equation, equation_1, equation_2 = None, None, None
if method == 4:
    equation_1, equation_2 = input_data.choose_equations()
else:
    equation = input_data.choose_equation()
input_format = input_data.choose_input_format()
a, b = 0, 0
a_1, b_1 = 0, 0
a_2, b_2 = 0, 0
accuracy = 0.1
max_iterations = 15
x0, y0 = 0, 0
if input_format == 2:
    file_name = input("Enter the file name: ")
    f = open(file_name, 'r')
    if method == 4:
        a_1, b_1 = input_data.choose_interval_from_file(f)
        a_2, b_2 = input_data.choose_interval_from_file(f)
        x0, y0 = input_data.choose_initial_approximation_from_file(f)
    else:
        a, b = input_data.choose_interval_from_file(f)
    accuracy = input_data.choose_accuracy_from_file(f)
    max_iterations = input_data.choose_max_iterations_from_file(f)
else:
    if method == 4:
        a_1, b_1 = input_data.choose_interval()
        a_2, b_2 = input_data.choose_interval()
        x0, y0 = input_data.choose_initial_approximation()
    else:
        a, b = input_data.choose_interval()
    accuracy = input_data.choose_accuracy()
    max_iterations = input_data.choose_max_iterations()
if method == 4:
    a_1, b_1 = input_data.validate_interval(a_1, b_1)
    a_2, b_2 = input_data.validate_interval(a_2, b_2)
else:
    a, b = input_data.validate_interval(a, b)
    if not check_for_roots(equation, a, b):
        exit()
x, y, itr, vector = None, None, None, None
match method:
    case 1:
        x, itr = methods.chord_method(equation, a, b, accuracy, max_iterations)
    case 2:
        x, itr = methods.secant_method(equation, a, b, accuracy, max_iterations)
    case 3:
        x, itr = methods.simple_iteration_method(equation, a, b, accuracy, max_iterations)
        if x is None or itr is None:
            exit()
    case 4:
        x, y, itr, vector = methods.simple_iteration_method_for_systems(equation_1, equation_2, a_1, b_1, a_2, b_2, x0, y0, accuracy, max_iterations)
        if x is None or itr is None or y is None:
            exit()
output_format = input_data.choose_output_format()
if output_format == 1:
    if method == 4:
        print("x = ", x, " y = ", y)
        print("Iterations: ", itr)
        print("x vector: ", vector[0])
        print("y vector: ", vector[1])
        print("Check: " + str(lambdify([q, w], eq[equation_1])(x, y)) + " " + str(lambdify([q, w], eq[equation_2])(x, y)))
    else:
        print("x = ", x)
        print("Iterations: ", itr)
else:
    file_name = input("Enter the file name: ")
    f = open(file_name, 'w')
    if method == 4:
        f.write("x = " + str(x) + " y = " + str(y))
        f.write("Iterations: " + str(itr))
        f.write("x vector: " + str(vector[0]))
        f.write("y vector: " + str(vector[1]))
        f.write("Check: " + lambdify([q, w], eq[equation_1])(x, y) + " " + lambdify([q, w], eq[equation_2])(x, y))
    else:
        f.write("x = " + str(x))
        f.write("Iterations: " + str(itr))
    f.close()
if method == 4:
    draw_graphic_for_systems(eq[equation_1], eq[equation_2], a_1, b_1, a_2, b_2, x, y)
else:
    draw_graphic(equation, a, b, x)
exit(0)
