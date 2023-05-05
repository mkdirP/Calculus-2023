import numpy as np


def line_approximation(dots):
    n = len(dots)
    x = [dot[0] for dot in dots]
    y = [dot[1] for dot in dots]
    sum_x = sum(x)
    sum_y = sum(y)
    sum_x2 = sum([x[i] ** 2 for i in range(n)])
    sum_xy = sum([x[i] * y[i] for i in range(n)])
    matrix = [[sum_x2, sum_x], [sum_x, n]]
    a, b = np.linalg.solve(matrix, [sum_xy, sum_y])
    result = {'a': a, 'b': b}
    f = lambda k: a * k + b
    result['f'] = f
    result['string_f'] = f'y = {round(a, 3)}x + {round(b, 3)}'
    result['variance'] = sum([(y[i] - f(x[i])) ** 2 for i in range(n)]) / n
