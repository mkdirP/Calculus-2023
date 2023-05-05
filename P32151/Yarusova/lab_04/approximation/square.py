
def square_approximation(dots):
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

