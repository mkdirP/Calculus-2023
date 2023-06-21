import sys
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
from interpolation.universal import *


def enter_float_array(message):
    inp_str = input(message + "\n")
    try:
        inp_str = inp_str.split(" ")
        for i in range(len(inp_str)):
            inp_str[i] = float(inp_str[i])
    except ValueError:
        print("Wrong float value in array")
        exit_program()
    return inp_str


def enter_float(message):
    user_input = input(message + "\n")
    try:
        user_input = float(user_input)
    except ValueError:
        print("Wrong float value")
        exit_program()
    return user_input


def enter_interval():
    inp_str = input("Enter interval as 2 numbers like this: 'a b'\n")
    try:
        inp_str = inp_str.split(" ")
        for i in range(len(inp_str)):
            inp_str[i] = float(inp_str[i])
    except ValueError:
        print("Wrong float value in array")
        exit_program()
    if len(inp_str) != 2:
        sys.exit("2 float arguments expected!")
    if inp_str[0] > inp_str[1]:
        inp_str[0], inp_str[1] = inp_str[1], inp_str[0]
    return inp_str


def exit_program():
    print("lol")
    sys.exit(0)


def draw_function_one_dot_one_simple_from_array(X, Y, results_array):
    plt.plot(X, Y, "ro")
    plt.plot(X, results_array)
    plt.axis([min(X)-min(X)/4, max(X)+max(X)/4, min(min(Y), min(results_array)) - min((min(Y), min(results_array)))/4, max(max(Y), max(results_array)) + max((max(Y), max(results_array)))/4])
    plt.show()


def draw_function_one_dot_one_simple_from_functions(a, b, h, f1, f2):
    X, Y1 = get_results_function(a, b, h, f1)
    Y2 = get_results_function(a, b, h, f2)[1]
    draw_function_one_dot_one_simple_from_array(X, Y1, Y2)


def draw_one_array_one_function(X, Y, f):
    x_interval = np.linspace(min(X)-min(X)/4, max(X)+min(X)/4, 100)
    y_interval = list(map(f, x_interval))
    plt.plot(X, Y, "ro")
    plt.plot(x_interval, y_interval)
    plt.axis([min(x_interval)-min(x_interval)/4, max(x_interval)+max(x_interval)/4, min(min(Y), min(y_interval)) - min((min(Y), min(y_interval)))/4, max(max(Y), max(y_interval)) + max((max(Y), max(y_interval)))/4])
    plt.show()

def read_file(link):
    if not (os.path.exists(link)):
        sys.exit("No such file exists")
    if not(os.path.isfile(link)):
        sys.exit("No such file")
    return pd.read_csv(link)

