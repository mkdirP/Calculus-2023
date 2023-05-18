import tools

def line(dots):
    n = len(dots)
    x = [dot[0] for dot in dots]
    y = [dot[1] for dot in dots]
    sum_x = sum(x)
    sum_y = sum(y)
    sum_x2 = sum([x[i] ** 2 for i in range(n)])
    sum_xy = sum([x[i] * y[i] for i in range(n)])
    a = (sum_xy * n - sum_x * sum_y) / (sum_x2 * n - sum_x ** 2)
    b = (sum_x2 * sum_y - sum_x * sum_xy) / (sum_x2 * n - sum_x ** 2)
    result = {'a': a, 'b': b}
    f = lambda k: a * k + b
    result['f'] = f
    result['string_f'] = f'y = {round(a, 3)}x + {round(b, 3)}'
    result['x'] = x
    result['y'] = y
    result['f(x)'] = [f(x[i]) for i in range(n)]
    result['variance'] = tools.variance(dots, f)
    result['standard_deviation'] = tools.standard_deviation(result['variance'])
    x_average = sum_x / n
    y_average = sum_y / n
    result['correlation_coefficient'] = sum([(x[i] - x_average) * (y[i] - y_average) for i in range(n)]) / (sum([(x[i] - x_average) ** 2 for i in range(n)]) * sum([(y[i] - y_average) ** 2 for i in range(n)])) ** 0.5
    return result
