import math


def f1(x):
    return (4 * x) / (x ** 4 + 3)


def f2(x):
    return x + 12


def f3(x):
    return x * x + 2 * x + 1


def f4(x):
    return x ** 3 + x - 10


def f5(x):
    return math.e ** (x ** 2 - x + 1)


def f6(x):
    if x <= 0:
        return 0
    else:
        return math.log(x, 2) + math.log(x, 3)
