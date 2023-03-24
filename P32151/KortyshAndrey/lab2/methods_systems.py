from sympy import *
import typing
from typing import Callable

x = Symbol('x')
y = Symbol('y')
available_systems = [
    tuple([  # x_0 = 0.5, y_0 = -1
        sin(2*x - y) - 1.2*x - 0.4,
        x**2 + y**2 - 1
    ]),
    tuple([  # x_0 = 0.5, y_0 = 0.2
        y - 0.5 * x**2 + x - 0.7,
        2 * x + y - 1/6 * y**3 - 1.6
    ])
]


def newton_method(x_0: float, y_0: float, epsilon: float, system: typing.Tuple[Add, Add]) -> \
        typing.Tuple[typing.Tuple[float, float], int, typing.Tuple[float, float], typing.Tuple[float, float]]:
    iteration_count = 0

    cur_x: float = x_0
    cur_y: float = y_0
    prev_x: float = 1e9
    prev_y: float = 1e9
    callable_f: Callable[[float, float], float] = lambdify([x, y], system[0], 'numpy')
    callable_g: Callable[[float, float], float] = lambdify([x, y], system[1], 'numpy')

    callable_f_diff_x: Callable[[float, float], float] = lambdify([x, y], system[0].diff(x), 'numpy')
    callable_f_diff_y: Callable[[float, float], float] = lambdify([x, y], system[0].diff(y), 'numpy')
    callable_g_diff_x: Callable[[float, float], float] = lambdify([x, y], system[1].diff(x), 'numpy')
    callable_g_diff_y: Callable[[float, float], float] = lambdify([x, y], system[1].diff(y), 'numpy')

    iteration_function_y: Callable[[float, float], float] = lambda x1, y1: (callable_f(x1, y1)*callable_g_diff_x(x1, y1)/callable_f_diff_x(x1, y1) - callable_g(x1, y1)) / \
                            (-callable_g_diff_x(x1, y1)*callable_f_diff_y(x1, y1)/callable_f_diff_x(x1, y1) + callable_g_diff_y(x1, y1))
    iteration_function_x: Callable[[float, float, float], float] = lambda x1, y1, delta_y1: (-callable_f_diff_y(x1, y1) * delta_y1 - callable_f(x1, y1)) / callable_f_diff_x(x1, y1)

    while abs(cur_x - prev_x) > epsilon or abs(cur_y - prev_y) > epsilon:
        delta_y: float = iteration_function_y(cur_x, cur_y)
        delta_x: float = iteration_function_x(cur_x, cur_y, delta_y)
        cur_x, prev_x, cur_y, prev_y = cur_x + delta_x, cur_x, cur_y + delta_y, cur_y
        iteration_count += 1
    return tuple([cur_x, cur_y]), iteration_count, tuple([cur_x - prev_x, cur_y - prev_y]), tuple([callable_f(cur_x, cur_y), callable_g(cur_x, cur_y)])
