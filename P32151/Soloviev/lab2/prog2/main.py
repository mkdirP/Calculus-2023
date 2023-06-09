import math
import sys
from prettytable import PrettyTable
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp


def from_file(path):
    f = open(path)
    tp = int(f.readline())
    if tp == 1:
        try:
            func = int(f.readline())
            method = int(f.readline())
            print_graph(func, -5, 5)
            while True:
                a = float(f.readline())
                b = float(f.readline())
                is_correct = f.readline()
                if is_correct == 'y':
                    break
            print_graph(func, a, b)
            e = float(f.readline())
            f.close()
            launch_method(method, func, a, b, e)
            return
        except:
            print("Error: Invalid file template")
            return
    elif tp == 2:
        try:
            first_func = f.readline()
            second_func = f.readline()
            print_system_graph(first_func, second_func)
            a, b = f.readline().split()
            e = f.readline()
            system_newton_method(first_func, second_func, a, b, e)
        except:
            print("Error: Invalid file template")
            return


# --- non-linear expressions ---
def get_func(num):
    if num == 1:
        return lambda x: 4.45 * x ** 3 + 7.81 * x ** 2 - 9.62 * x - 8.17
    if num == 2:
        return lambda x: x ** 3 - 4.5 * x ** 2 - 9.21 * x - 0.383
    if num == 3:
        return lambda x: x ** 3 + 4.81 * x ** 2 - 17.37 * x + 5.38
    if num == 4:
        return lambda x: 0.7 * np.cos(x) * np.sin(1.3 * x)


def get_func_name(num):
    if num == 1:
        return "4.45*x^3 + 7.81*x^2 − 9.62*x − 8.17"
    if num == 2:
        return "x^3 - 4.81*x^2 − 17.37*x + 5.38"
    if num == 3:
        return "x^3 − 4.5*x^2 − 9.21*x − 0.383"
    if num == 4:
        return "0.7*cos(x) * sin(1.3*x)"


def get_method(num):
    if num == 1:
        return "half division method"
    if num == 2:
        return "secant method"
    if num == 3:
        return "iterations method"


#     if count_roots < 1:
#         print("\033[31m{}".format("Error: There are no root on this segment"))
#         print("\033[0m".format(), end='')
#         return
def choose_func():
    while True:
        try:
            print("Choose functions:")
            for i in [1, 2, 3, 4]:
                print(str(i) + ")", get_func_name(i))
            chosen_func = int(input(">>>"))
            if chosen_func in [1, 2, 3, 4]:
                print("\033[34m{}".format("Chosen function:"), get_func_name(chosen_func))
                print("\033[0m".format(), end='')
                break
            print("\033[31m{}".format("Error: Wrong input. Chose int number between 1 and 4."))
            print("\033[0m".format(), end='')
        except:
            print("\033[31m{}".format("Error: Wrong input. Chose INT NUMBER between 1 and 4."))
            print("\033[0m".format(), end='')
            pass
    return get_func(chosen_func)


def choose_method():
    while True:
        try:
            print("Choose method:")
            for i in [1, 2, 3]:
                print(str(i) + ")", get_method(i))
            chosen_method = int(input(">>>"))
            if chosen_method in [1, 2, 3]:
                print("\033[34m{}".format("Chosen method:"), get_method(chosen_method))
                print("\033[0m".format(), end='')
                break
            print("\033[31m{}".format("Error: Wrong input. Chose int number between 1 and 4."))
            print("\033[0m".format(), end='')
        except:
            print("\033[31m{}".format("Error: Wrong input. Chose INT NUMBER between 1 and 3."))
            print("\033[0m".format(), end='')
            pass
    return chosen_method


# --- non-linear expressions ---
def get_system_func(num):
    if num == 1:
        return lambda x, y: x ** 2 + y ** 2 - 4
    if num == 2:
        return lambda x, y: x ** 3 + y - 1
    if num == 3:
        return lambda x, y: x ** 2 - y - 3


def get_system_func_name(num):
    if num == 1:
        return "x^2 + y^2 - 4"
    if num == 2:
        return "x^3 + y - 1"
    if num == 3:
        return "x^2 - y - 3"


def build_system():
    while True:
        try:
            print("Select first function for the system:")
            for i in [1, 2, 3]:
                print(str(i) + ")", get_system_func_name(i))
            first = int(input(">>>"))
            if first not in [1, 2, 3]:
                print("\033[31m{}".format("Error: Wrong input. Re-enter."))
                print("\033[0m".format(), end='')
            else:
                print("Select second function for the system:")
                for i in [1, 2, 3]:
                    print(str(i) + ")", get_system_func_name(i))
                second = int(input(">>>"))
                if second not in [1, 2, 3]:
                    print("\033[31m{}".format("Error: Wrong input. Re-enter from the beginning."))
                    print("\033[0m".format(), end='')
                print("\033[34m{}".format("Chosen functions:\n"), get_system_func_name(first), "\n",
                      get_system_func_name(second))
                print("\033[0m".format(), end='')
                if second == first:
                    print("\033[31m{}".format("Error: Functions cannot be the same"))
                    print("\033[0m".format(), end='')
                return get_system_func(first), get_system_func(second)
        except:
            print("\033[31m{}".format("Error: Wrong input. Re-enter."))
            print("\033[0m".format(), end='')
            pass


def input_error():
    while True:
        try:
            print("Enter an accuracy that is a multiple of a power of 10")
            e = float(input(">>>"))
            if e > 0 and math.log10(e) == int(math.log10(e)):
                print("\033[34m{}".format("Chosen accuracy:"), e)
                print("\033[0m".format(), end='')
                return e
            print("\033[31m{}".format("Error: Wrong input. Chose float number lower than 0 and that is a multiple of "
                                      "a power of 10"))
            print("\033[0m".format(), end='')
        except:
            print("\033[31m{}".format("Error: Wrong input. Chose FLOAT NUMBER lower than 0 and that is a multiple of "
                                      "a power of 10"))
            print("\033[0m".format(), end='')
            pass


def launch_method(num, func, a, b, e):
    if num == 1:
        half_division_method(func, a, b, e)
    if num == 2:
        secant_method(func, a, b, e)
    if num == 3:
        iterations_method(func, a, b, e)


def input_borders():
    while True:
        try:
            print("Enter the left border of the interval")
            a = float(input(">>>"))
            print("Enter the right border of the interval")
            b = float(input(">>>"))
            if a >= b:
                print("Invalid input. Left_border >= Right_border. Re-try input.")
            else:
                return a, b
        except:
            print("\033[31m{}".format("Error: invalid input. Re-try input"))
            print("\033[0m".format(), end='')
            pass


def get_approx():
    while True:
        try:
            print("Enter the initial approximation separated by a space")
            a, b = map(float, input(">>>").split())
            break
        except:
            print("The initial guess must be space-separated numbers.")
    return a, b


def partial_derivative_x(func, x, y, h=0.00000001):
    return (func(x + h, y) - func(x - h, y)) / (2 * h)


def partial_derivative_y(func, x, y, h=0.00000001):
    return (func(x, y + h) - func(x, y - h)) / (2 * h)


def find_div(function, h=0.000000001):
    return lambda x: (function(x + h) - function(x - h)) / (2 * h)


def system_determinant(first_func, second_func, x, y):
    return partial_derivative_x(first_func, x, y) * partial_derivative_y(second_func, x, y) - partial_derivative_x(
        second_func, x, y) * partial_derivative_y(first_func, x, y)


def print_graph(func, a, b):
    x = np.linspace(a, b, 1000000)
    y = func(x)
    x1 = [a, a]
    x2 = [b, b]
    y1 = [-20, 20]
    plt.plot(x, y, '-', x1, y1, '--', x2, y1, '--')
    plt.grid()
    plt.show()


def print_system_graph(first_func, second_func):
    x, y = sp.symbols("x y")
    sp.plot_implicit(sp.Or(sp.Eq(first_func(x, y), 0), sp.Eq(
        second_func(x, y), 0)))
    # x = np.linspace(a, b, 1000000)
    # y = np.linspace(-5, 5, 1000000)
    # first_y = first_func(x, y)
    # second_y = second_func(x, y)
    # plt.plot(first_y, '-', second_y, "-")
    # plt.grid()
    # plt.show()


def print_result_point(func, x, a, b, e):
    x = np.linspace(x-e, x+e)
    y = func(x)
    mask = np.abs(y) < e
    x1 = [a, a]
    x2 = [b, b]
    y1 = [-5, 5]
    x_f = np.linspace(a, b, 1000000)
    y_f = func(x_f)
    plt.plot(x_f, y_f, '-', x1, y1, '--', x2, y1, '--')
    plt.scatter(x[mask], y[mask], color='orange', s=40, marker='o')
    plt.grid()
    plt.show()


# ---methods---
def half_division_method(func, a, b, e):
    th = ["n", "a", "b", "x", "f(a)", "f(b)", "f(x)", "|a-b|"]
    table = PrettyTable(th)
    n = 0
    i = a + e
    count_roots = 0
    lb = a
    rb = b
    while i < b:
        if func(i - e) * func(i) < 0:
            count_roots += 1
        if count_roots > 1:
            print("\033[31m{}".format("Error: There are more than one root on this segment"))
            print("\033[0m".format(), end='')
            return
        i += e
    print("\033[34m{}".format("Half division method:"))
    print("\033[0m".format(), end='')
    while True:
        x = (a + b) / 2
        td = [round(n, int(abs(math.log10(e)))), round(a, int(abs(math.log10(e)))),
              round(b, int(abs(math.log10(e)))),
              round(x, int(abs(math.log10(e)))), round(func(a), int(abs(math.log10(e)))),
              round(func(b), int(abs(math.log10(e)))),
              round(func(x), int(abs(math.log10(e)))),
              round(abs(a - b), int(abs(math.log10(e))))]
        table.add_row(td)
        if func(a) * func(x) > 0:
            a = x
        else:
            b = x
        if (round(abs(a - b), int(abs(math.log10(e)))) <= e) or (
                round(abs(func(x)), int(abs(math.log10(e)))) <= e):
            print(table)
            print("\033[32m{}".format("result: x ="), round(x, int(abs(math.log10(e)))), ",f(x) =",
                  round(func(x), int(abs(math.log10(e)))), ",n =", n)
            print("\033[0m".format(), end='')
            print_result_point(func, x, lb, rb,e)
            break
        n += 1


def secant_method(func, a, b, e):
    i = a + e
    lb, rb = a, b
    count_roots = 0
    while i < b:
        if func(i - e) * func(i) < 0:
            count_roots += 1
        if count_roots > 1:
            print("\033[31m{}".format("Error: There are no roots or more than one root on this segment"))
            print("\033[0m".format(), end='')
            return
        i += e
    x_prev_prev = 0
    x_prev = 0
    th = ["n", "x_k-1", "x_k", "x_(k+1)", "f(x_(k+1))", "|x_(k+1) - x_k|"]
    table = PrettyTable(th)
    # Find first approximation
    if func(a) * find_div(find_div(func))(a) > 0:
        print("The first approximation number: " + str(a))
        x_prev_prev = a
        x_prev = a + e
    else:
        print("The first approximation number: " + str(b))
        x_prev_prev = b
        x_prev = b - e
    n = 0
    # Find roots, catch stop expression
    while abs((func(x_prev))) > e:
        x_current = x_prev - ((x_prev - x_prev_prev) / (func(x_prev) - func(x_prev_prev))) * func(x_prev)
        x_prev_prev = x_prev
        x_prev = x_current
        td = [n, round(x_prev_prev, int(abs(math.log10(e)))), round(x_prev, int(abs(math.log10(e)))),
              round(x_current, int(abs(math.log10(e)))),
              round(func(x_current), int(abs(math.log10(e)))),
              round(abs(x_current - x_prev), int(abs(math.log10(e))))]
        table.add_row(td)
        n += 1

    print_result_point(func, x_current, lb, rb, e)
    print(table)
    print("\033[32m{}".format("result: x ="), round(x_current, int(abs(math.log10(e)))), ",f(x) =",
          round(func(x_current), int(abs(math.log10(e)))), ",n =", n)
    print("\033[0m".format(), end='')


def iterations_method(func, a, b, e):
    i = a + e
    lb, rb = a, b
    count_roots = 0
    while i < b:
        if func(i - e) * func(i) < 0:
            count_roots += 1
        if count_roots > 1:
            print("\033[31m{}".format("Error: There are no roots or more than one root on this segment"))
            print("\033[0m".format(), end='')
            return
        i += e
    dev_a = find_div(func)(a)
    dev_b = find_div(func)(b)
    print("Derivative at a point A: " + str(dev_a))
    print("Derivative at a point B: " + str(dev_b))
    lyambd_a = -(1 / dev_a)
    lyambd_b = - (1 / dev_b)
    print("Lambda А =", lyambd_a)
    print("Lambda B =", lyambd_b)
    if dev_a > dev_b:
        lyambd = lyambd_a
    else:
        lyambd = lyambd_b
    fi = lambda x: x + lyambd * func(x)
    fi_s = find_div(fi)
    fi_s_a = fi_s(a)
    fi_s_b = fi_s(b)
    print("Derivative phi at a point А: ", fi_s_a)
    print("Derivative phi at a point А:", fi_s_b)
    if abs(fi_s(a)) > 1 or abs(fi_s(b)) > 1:
        print("\033[31m{}".format("Error: Does not satisfy a sufficient convergence condition"))
        print("\033[0m".format(), end='')
    else:
        print("\033[32m{}".format("Satisfies the sufficient convergence condition"))
        print("\033[0m".format(), end='')
    x_current = a
    x_prev = a * 1000 + 10
    iterations = 0
    th = ["n", "x_k", "x_(k+1)", "f(x_(k+1))", "|x_(k+1) - x_k|"]
    table = PrettyTable(th)

    # find roots
    n = 0
    while (abs(x_prev - x_current) > e) or (abs(func(x_current)) > e):
        x_prev = x_current
        x_current = x_prev + lyambd * func(x_prev)
        iterations += 1
        if iterations > 1000:
            print("\033[31m{}".format("The algorithm diverges"))
            print("\033[0m".format(), end='')
            exit()
        td = [n, round(x_prev, int(abs(math.log10(e)))), round(x_current, int(abs(math.log10(e)))),
              round(func(x_current), int(abs(math.log10(e)))),
              round(abs(x_current - x_prev), int(abs(math.log10(e))))]
        table.add_row(td)
        n += 1
    print(table)
    print_result_point(func, x_current, lb, rb, e)
    print("\033[32m{}".format("result: x ="), round(x_current, int(abs(math.log10(e)))), ",f(x) =",
          round(func(x_current), int(abs(math.log10(e)))), ",n =", n - 1)
    print("\033[0m".format(), end='')


def system_newton_method(first_func, second_func, a, b, e):
    try:
        x_current = a
        y_current = b
        y_prev = y_current * 1000 + 10
        x_prev = x_current * 1000 + 10
        n = 0
        th = ["n", "x_i", "y_i", "|x_i - x_(i-1)|", "|y_i - y_(i-1)|"]
        table = PrettyTable(th)
        while max(abs(x_current - x_prev), abs(y_current - y_prev)) > e:
            x_prev = x_current
            y_prev = y_current
            J = system_determinant(first_func, second_func, x_prev, y_prev)
            A = first_func(x_prev, y_prev) / J
            B = second_func(x_prev, y_prev) / J
            x_current = x_prev - A * partial_derivative_y(second_func, x_prev, y_prev) + B * partial_derivative_y(
                first_func, x_prev, y_prev)
            y_current = y_prev + A * partial_derivative_x(second_func, x_prev, y_prev) - B * partial_derivative_x(
                first_func, x_prev, y_prev)
            n += 1
            if n == 100:
                print("\033[31m{}".format("Algorithm divergent"))
                exit()
            td = [n, round(x_current, int(abs(math.log10(e)))), round(y_current, int(abs(math.log10(e)))),
                  round(abs(x_current - x_prev), int(abs(math.log10(e)))),
                  round(abs(y_current - y_prev), int(abs(math.log10(e))))]
            table.add_row(td)
        print(table)
        print("\033[32m{}".format("result: x ="), round(x_current, int(abs(math.log10(e)))), "; y =",
              round(y_current, int(abs(math.log10(e)))))
        print("\033[0m".format(), end='')
    except:
        print("\033[31m{}".format("There are no roots or more than one root on this segment"))
        print("\033[0m".format(), end='')
        return False
    return True


def main():
    print("\033[31m\033[40m{}".format("Soloviev Artemiy P32151"))
    print("Task option 11")
    print("\033[0m".format())
    # to read from file run with key -f
    # in this form: python main.py -f *path*
    if len(sys.argv) == 3:
        try:
            if sys.argv[1] == "-f":
                from_file(sys.argv[2])
        except:
            print("Error: invalid path")
    else:
        while True:
            try:
                print("Choose type:\n"
                      "1) Non-linear functions\n"
                      "2) System of non-linear functions")
                chosen_type = int(input(">>>"))
                if chosen_type == 1:
                    print("\033[34m{}".format("Chosen type: Non-linear functions"))
                    print("\033[0m".format(), end='')
                    break
                elif chosen_type == 2:
                    print("Chosen type: System of non-linear functions")
                    break
                else:
                    print("\033[31m{}".format("Error: Wrong input. Chose int number between 1 and 2."))
                    print("\033[0m".format(), end='')
            except:
                print("\033[31m{}".format("Error: Wrong input. Chose INT NUMBER between 1 and 2."))
                print("\033[0m".format(), end='')
                pass
        if chosen_type == 1:
            func = choose_func()
            method = choose_method()
            print("\033[32m{}".format("Function graph is on your screen!"))
            print("\033[0m".format(), end='')
            print_graph(func, -5, 5)
            while True:
                a, b = input_borders()
                print_graph(func, a, b)
                print("Look at the screen\nIs this the correct interval?(y/n)")
                is_correct = input(">>>")
                if is_correct == 'y':
                    print("\033[34m{}".format("Chosen interval: [" + str(a) + ":" + str(b) + "]"))
                    print("\033[0m".format(), end='')
                    break
            e = input_error()

            launch_method(method, func, a, b, e)
        if chosen_type == 2:
            first_func, second_func = build_system()
            print_system_graph(first_func, second_func)
            print("\033[32m{}".format("Function graph is on your screen!"))
            print("\033[0m".format(), end='')
            while True:
                a, b = get_approx()
                e = input_error()
                is_all_good = system_newton_method(first_func, second_func, a, b, e)
                if is_all_good:
                    break
                print("\033[31m{}".format("Error: Wrong interval. re-enter."))
                print("\033[0m".format(), end='')


if __name__ == '__main__':
    main()
