import numpy as np
import tools

def square(dots):
    n = len(dots)
    x = [dot[0] for dot in dots]
    y = [dot[1] for dot in dots]
    sum_x = sum(x)
    sum_y = sum(y)
    sum_x2 = sum([x[i] ** 2 for i in range(n)])
    sum_xy = sum([x[i] * y[i] for i in range(n)])
    sum_x3 = sum([x[i] ** 3 for i in range(n)])
    sum_x4 = sum([x[i] ** 4 for i in range(n)])
    sum_x2y = sum([x[i] ** 2 * y[i] for i in range(n)])
    # a0 + a1 * x + a2 * x^2 = y
    # a0 * n + a1 * sum_x + a2 * sum_x2 = sum_y
    # a0 * sum_x + a1 * sum_x2 + a2 * sum_x3 = sum_xy
    # a0 * sum_x2 + a1 * sum_x3 + a2 * sum_x4 = sum_x2y
    right_matrix = np.array([[n, sum_x, sum_x2], [sum_x, sum_x2, sum_x3], [sum_x2, sum_x3, sum_x4]])
    left_matrix = np.array([sum_y, sum_xy, sum_x2y])
    a = np.linalg.solve(right_matrix, left_matrix)
    result = {'a0': a[0], 'a1': a[1], 'a2': a[2]}
    f = lambda k: a[0] + a[1] * k + a[2] * k ** 2
    result['f'] = f
    result['string_f'] = f'y = {round(a[0], 3)} + {round(a[1], 3)}x + {round(a[2], 3)}x^2'
    result['x'] = x
    result['y'] = y
    result['f(x)'] = [f(x[i]) for i in range(n)]
    result['variance'] = tools.variance(dots, f)
    result['standard_deviation'] = tools.standard_deviation(result['variance'])
    return result
