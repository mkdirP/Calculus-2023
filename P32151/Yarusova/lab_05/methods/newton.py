import pandas as pd
from math import factorial


def newton(data, interpolation_dot):
    n = len(data['x'])
    x = data['x']
    y = data['y']
    h = check_h_is_constant(x)
    difference = count_difference(x, y)
    print(pd.DataFrame(difference).to_latex())
    if interpolation_dot <= x[n // 2]:
        print("Newton interpolation forward")
        x0 = find_x0(x, interpolation_dot)
        t = (interpolation_dot - x[0]) / h
        result = difference[x0][0]
        for i in range(1, n):
            result += taylor_forward(t, i, difference[x0][i])

    else:
        print("Newton interpolation backward")
        t = (interpolation_dot - x[n - 1]) / h
        result = difference[n - 1][0]
        for i in range(1, n):
            result += taylor_backward(t, i, difference[n - 1 - i][i])
    return result


def check_h_is_constant(x):
    h = x[1] - x[0]
    for i in range(2, len(x)):
        if x[i] - x[i - 1] != h:
            raise ValueError("h is not constant")
    return h


def count_difference(x, y):
    n = len(x)
    difference = [[0] * n for _ in range(n)]
    for i in range(n):
        difference[i][0] = y[i]
    for j in range(1, n):
        for i in range(n - j):
            difference[i][j] = difference[i + 1][j - 1] - difference[i][j - 1]
    return difference


def find_x0(x, interpolation_dot):
    n = len(x)
    x0 = n - 1
    for i in range(n):
        if x[i] >= interpolation_dot:
            x0 = i - 1
    if x0 < 0:
        x0 = 0
    return x0


def taylor_forward(t0, i, difference):
    taylor_div = difference / factorial(i)
    t = t0
    for j in range(1, i):
        t *= (t0 - j)
    return taylor_div * t


def taylor_backward(t0, i, difference):
    taylor_div = difference / factorial(i)
    t = t0
    for j in range(1, i):
        t *= (t0 + j)
    return taylor_div * t
