import sys

import matplotlib.pyplot as plt
import numpy as np
import math


def check_interval(func, a, b):
    print("f(a):%f", func(a))
    print("f(b):%f", func(b))
    if func(a) * func(b) < 0:
        return True
    else:
        return False


def chords(func, a, b):
    if check_interval(func, a, b) == False:
        return "Неправильный интервал!"

    xnpy = np.linspace(a, b, 100)
    ynpy = func(xnpy)
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    plt.plot(xnpy, ynpy, 'g')


    eps = float(input("Введите эпсилон:\n").replace(",", "."))
    x = 0
    while abs(a - b) > eps:
        fa = func(a)
        fb = func(b)

        x = (a * fb - b * fa) / (fb - fa)
        fx = func(x)
        if fa * fx > 0 > fb * fx:
            a = x
        elif fb * fx > 0 > fa * fx:
            b = x
        elif func(x) == 0:
            plt.plot(x, func(x), 'ro')
            plt.show()
            return x
        else:
            sys.exit("В методе хорд произошла ошибка\n")
    plt.plot(x, func(x), 'ro')
    plt.show()
    return x


def simple_iter(func, a, b):

    if (check_interval(func, a, b) == False):
        return "Неправильный интервал!"

    xnpy = np.linspace(a, b, 100)
    ynpy = func(xnpy)
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    plt.plot(xnpy, ynpy, 'g')

    eps = float(input("Введите эпсилон:\n").replace(",", "."))
    deriv_a = (func(a + eps / 100) - func(a)) / (eps / 100)
    deriv_b = (func(b + eps / 100) - func(b)) / (eps / 100)
    if (deriv_a > deriv_b):
        max_deriv = deriv_a
        xi = a
    else:
        max_deriv = deriv_b
        xi = b
    lamda = -1 / max_deriv
    itercount = 0
    while (abs(xi + lamda * func(xi) - xi) > eps):
        if itercount > 1000:
            return xi + lamda * func(xi)
        xi = xi + lamda * func(xi)
        itercount += 1
    plt.plot(xi + lamda * func(xi), func(xi + lamda * func(xi)), 'ro')
    plt.show()
    return xi + lamda * func(xi)


def sec(func, a, b):

    if (check_interval(func, a, b) == False):
        return "Неправильный интервал!"

    xnpy = np.linspace(a, b, 100)
    ynpy = func(xnpy)
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    plt.plot(xnpy, ynpy, 'g')

    eps = float(input("Введите эпсилон:\n").replace(",", "."))

    xi_2 = b
    xi_1 = b - abs(b-a)/8
    xi = xi_1 - func(xi_1)*(xi_1-xi_2)/(func(xi_1)-func(xi_2))

    while abs(xi - xi_1) <= eps:
        tmp_1 = xi
        tmp_2 = xi_1
        xi = xi_1 - func(xi_1)*(xi_1-xi_2)/(func(xi_1)-func(xi_2))
        xi_2 = tmp_2
        xi_1 = tmp_1
    plt.plot(xi, func(xi), 'ro')
    plt.show()
    return xi
