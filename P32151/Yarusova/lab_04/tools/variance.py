def variance(dots, f):
    n = len(dots)
    x = [dot[0] for dot in dots]
    y = [dot[1] for dot in dots]
    return [(f(x[i]) - y[i]) for i in range(n)]


def standard_deviation(variance_dots):
    n = len(variance_dots)
    return (sum([variance_dots[i] ** 2 for i in range(n)]) / n) ** 0.5
