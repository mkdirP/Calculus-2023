#ПОДСЧЕТ ПЛОЩАДИ ОДНОГО СЕТОРА
def squad_method_mid(func, a, b):
    return func((a + b) / 2) * (b - a)
    #подсчёт площади одного интервала методом среднего прямоугольника


def squad_method_left(func, a, b):
    return func(a) * (b - a)
    #методом левого прямоугольника


def squad_method_right(func, a, b):
    return func(b) * (b - a)
    #методом правого прямоугольника


def trapezoid_method(func, a, b):
    return ((func(a) + func(b)) / 2) * (b - a)
    #методом трапеции


def simpson_method(func, a, b):
    return ((b - a) / 6) * (func(a) + 4 * func((a + b) / 2) + func(b))

# ВЫЧИСЛЕНИЕ ИНТЕГРАЛЛА
def calc_integral(func, method_func, a, b, error, k):
    n = 4
    integral = -10
    integral_prev = error * 2
    while abs((integral_prev - integral) / (2 ** k - 1)) > error:
        integral_prev = integral
        integral = 0
        h = (abs(a - b)) / n
        for i in range(n):
            integral += method_func(func, a + h * i, a + h * (i + 1))
        n *= 2

    return integral, n / 2, abs((integral_prev - integral) / (2 ** k - 1))
