import sys
import matplotlib.pyplot as plt
from parsers import type_parser
from approximation.universal import *


def enter_float_array(message):
    return type_parser.parse_float_array(input(message + "\n"))


def enter_float(message):
    user_input = input(message + "\n")
    return type_parser.parse_float(user_input)


def enter_interval():
    user_input = input("Enter interval as 2 numbers like this: 'a b'\n")
    answer = type_parser.parse_float_array(user_input)
    if len(answer) != 2:
        sys.exit("2 float arguments expected!")
    if answer[0] > answer[1]:
        answer[0], answer[1] = answer[1], answer[0]
    return answer


def exit_program():
    print("Thank you for your time, bye!!!")
    sys.exit(0)


def draw_function_one_dot_one_simple_from_array(X, Y, results_array):
    plt.plot(X, Y)
    plt.plot(X, results_array, "ro")
    plt.axis([min(X), max(X), min(min(Y), min(results_array)), max(max(Y), max(results_array))])
    plt.show()


def draw_function_one_dot_one_simple_from_functions(a, b, h, f1, f2):
    X, Y1 = get_results_function(a, b, h, f1)
    Y2 = get_results_function(a, b, h, f2)[1]
    draw_function_one_dot_one_simple_from_array(X, Y1, Y2)
