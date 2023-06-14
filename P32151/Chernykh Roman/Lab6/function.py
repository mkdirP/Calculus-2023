import math


def get_func(num):
    if num == 1:
        return lambda x, y: math.cos(y) + 6 * x
    if num == 2:
        return lambda x, y: math.sin(x ** 2) + y + 6
    if num == 3:
        return lambda x, y: x**2 - 6 * y**2
    if num == 4:
        return lambda x, y: (x - y) ** 3


def get_str_func(num):
    if num == 1:
        return "cos(y) + 6x"
    if num == 2:
        return "sin(x^2) + y + 6"
    if num == 3:
        return "x^2 - 6y^2"
    if num == 4:
        return "(x - y)^3"