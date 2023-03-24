import typing
from typing import Callable, List
from sympy import *

# Methods: 2, 4, 5, 6
# хорд, секущих, простой итерации
# ньютона - для систем

x = Symbol('x')
available_functions: List[Add] = [
    cos(0.5*x) + sin(0.5*x) - 0.5,
    3*x - exp(x) + 5,
    x**3 - 0.1*x**2 + 0.5,
    2*x - cos(3*x) - 5
]


def count_solutions(a: float, b: float, function: Callable[[float], float]) -> int:
    step = 0.01
    cur_st = a
    cur_end = a + step
    solutions = 0
    while cur_end <= b:
        if function(cur_st) * function(cur_end) <= 0:
            solutions += 1
        cur_st += step
        cur_end += step
    return solutions


def check_common(a: int, b: int, function: Callable[[float], float]) -> bool:
    if a > b:
        return False
    if function(a) * function(b) > 0:
        return False
    return count_solutions(a, b, function) == 1


def chord_method(a: int, b: int, epsilon: float, function: Add) -> typing.Tuple[float, float, int]:
    iteration_count: int = 0
    callable_function = lambdify(x, function, 'numpy')

    if not check_common(a, b, callable_function):
        raise ValueError

    iteration_function: Callable[[float, float], float] = lambda c, d: (c * callable_function(d) - d * callable_function(c))\
                                                                       / (callable_function(d) - callable_function(c))
    cur_x: float = iteration_function(a, b)
    prev_x: float = 1e9
    while abs(prev_x - cur_x) > epsilon and abs(b - a) > epsilon and abs(callable_function(cur_x)) > epsilon:
        if callable_function(cur_x) * callable_function(a) < 0:
            b = cur_x
        else:
            a = cur_x
        prev_x = cur_x
        cur_x = iteration_function(a, b)
        iteration_count += 1
    return cur_x, callable_function(cur_x), iteration_count


def secant_method(a: int, b: int, epsilon: float, function: Add) -> typing.Tuple[float, float, int]:
    iteration_count: int = 0
    callable_function = lambdify(x, function, 'numpy')

    if not check_common(a, b, callable_function):
        raise ValueError

    second_derivative = lambdify(x, function.diff(x).diff(x), 'numpy')
    if callable_function(a) * second_derivative(a) > 0:
        prev_x = a
        cur_x = a+2*epsilon
    else:
        prev_x = b
        cur_x = b - 2*epsilon
    iteration_function: Callable[[float, float], float] = lambda prev_y, prev_prev_y: prev_y - callable_function(prev_y) * (prev_y - prev_prev_y) /\
                                                     (callable_function(prev_y) - callable_function(prev_prev_y))
    while abs(cur_x - prev_x) > epsilon and abs(callable_function(cur_x)) > epsilon:
        cur_x, prev_x = iteration_function(cur_x, prev_x), cur_x
        iteration_count += 1
    return cur_x, callable_function(cur_x), iteration_count


class SimpleIterationException(Exception):
    pass


def simple_iteration(a: int, b: int, epsilon: float, function: Add) -> typing.Tuple[float, float, int]:
    iteration_count: int = 0
    callable_function = lambdify(x, function, 'numpy')

    if not check_common(a, b, callable_function):
        raise ValueError

    first_derivative = lambdify(x, function.diff(x), 'numpy')

    coefficient = -1/max(abs(first_derivative(a)), abs(first_derivative(b)))
    if abs(1+coefficient*first_derivative(a)) >= 1 or abs(1+coefficient*first_derivative(b)) >= 1:
        raise SimpleIterationException

    iteration_function: Callable[[float], float] = lambda y: y + coefficient*callable_function(y)
    prev_x = 1e9
    cur_x = a if abs(first_derivative(a)) > abs(first_derivative(b)) else b
    while abs(callable_function(cur_x)) > epsilon and abs(cur_x - prev_x) > epsilon:
        cur_x, prev_x = iteration_function(cur_x), prev_x
        iteration_count += 1
    return cur_x, callable_function(cur_x), iteration_count
