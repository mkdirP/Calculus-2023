from sympy import Symbol, sin, exp, cos, Add, lambdify
from typing import Callable, List

x = Symbol("x")
y = Symbol("y")
C = Symbol("C")


def get_current_solution(equation_number: int, x_0: float, y_0: float) -> Add:
    if equation_number < 0 or equation_number >= len(equations):
        raise ValueError
    general_solution = exact_solution[equation_number]
    lambda_for_const = lambdify([x, y], expression_for_constant[equation_number], 'numpy')
    const = lambda_for_const(x_0, y_0)
    partial_solution = general_solution.subs({C: const})
    return partial_solution


def solve_single_turn(method: Callable[[Callable[[float, float], float], float, float, float], float],
                      equation_number: int, x_0: float, y_0: float, h: float, x_n: float, epsilon: float, rang: int) -> List[float]:
    ys = [y_0]
    cur_x = x_0
    cur_h = h
    y_h = 1e9
    y_h_2 = -1e9
    cur_y = y_0
    while abs(cur_x - x_n) > epsilon:
        while abs(y_h - y_h_2) / (2**rang - 1) > epsilon:
            y_h = solve_without_correction(method, equation_number, cur_x, cur_y, cur_h, cur_x+h, epsilon)[-1]
            y_h_2 = solve_without_correction(method, equation_number, cur_x, cur_y, cur_h/2, cur_x+h, epsilon)[-1]
            cur_h /= 2
        ys.append(y_h_2)
        cur_x += h
        cur_y = ys[-1]
        y_h = 1e9
        y_h_2 = -1e9
        cur_h = h
    return ys


def solve_without_correction(method: Callable[[Callable[[float, float], float], float, float, float], float],
                             equation_number: int, x_0: float, y_0: float, h: float, x_n: float, epsilon: float) -> List[float]:
    f_x_y = lambdify([x, y], equations[equation_number], 'numpy')
    ys = [y_0]
    cur_x = x_0
    while abs(cur_x - x_n) > epsilon:
        y_h = method(f_x_y, cur_x, ys[-1], h)
        ys.append(y_h)
        cur_x += h
    return ys


def modified_euler(f_x_y: Callable[[float, float], float], x_0: float, y_0: float, h: float) -> float:
    return y_0 + h/2*(f_x_y(x_0, y_0) + f_x_y(x_0 + h, y_0 + h*f_x_y(x_0, y_0)))


def runge_kutt(f_x_y: Callable[[float, float], float], x_0: float, y_0: float, h: float) -> float:
    k1 = h * f_x_y(x_0, y_0)
    k2 = h*f_x_y(x_0 + h / 2, y_0 + k1 / 2)
    k3 = h*f_x_y(x_0 + h / 2, y_0 + k2 / 2)
    k4 = h*f_x_y(x_0 + h, y_0 + k3)
    return y_0 + 1/6*(k1 + 2*k2 + 2*k3 + k4)


def adams(equation_number: int, x_0: float, y_0: float, h: float, x_n: float, epsilon) -> List[float]:
    f_x_y = lambdify([x, y], equations[equation_number], 'numpy')
    first_four = solve_single_turn(runge_kutt, equation_number, x_0, y_0, h, x_0 + 3*h, 0.001, 4)
    ys = first_four[::]
    last_four_xs = [x_0 + i*h for i in range(4)]
    last_four_ys = first_four[::]
    last_four_funcs = [f_x_y(x_i, y_i) for x_i, y_i in zip(last_four_xs, last_four_ys)]
    cur_x = x_0 + 3*h
    while abs(cur_x + h - x_n) < epsilon or cur_x + h < x_n:
        delta = last_four_funcs[-1] - last_four_funcs[-2]
        delta_sq = last_four_funcs[-1] - 2 * last_four_funcs[-2] + last_four_funcs[-3]
        delta_cube = last_four_funcs[-1] - 3 * last_four_funcs[-2] + 3 * last_four_funcs[-3] - last_four_funcs[-4]
        cur_y = last_four_ys[-1] + h * last_four_funcs[-1] + h**2/2 * delta + 5/12*h**3*delta_sq + 3/8*h**4*delta_cube
        last_four_funcs.pop(0)
        last_four_xs.pop(0)
        last_four_ys.pop(0)
        cur_x += h
        ys.append(cur_y)
        last_four_xs.append(cur_x)
        last_four_ys.append(cur_y)
        last_four_funcs.append(f_x_y(cur_x, cur_y))
    return ys


def get_errors(exact_ys: List[float], solution_ys: List[float]) -> List[float]:
    return [abs(y_1 - y_2) for y_1, y_2 in zip(exact_ys, solution_ys)]


equations = [
    -2*x*y + sin(x) * exp(-x**2),
    exp(-x)*x**2-y,
    -3*y*x**2 + cos(x)*exp(-x**3)
]

exact_solution = [
    -cos(x)*exp(-x**2) + C * exp(-x**2),
    x**3/3*exp(-x) + C*exp(-x),
    (sin(x) + C) * exp(-x**3)
]

expression_for_constant = [
    (y + cos(x)*exp(-x**2)) / exp(-x**2),
    (y - x**3/3*exp(-x)) / exp(-x),
    (y - sin(x) * exp(-x**3)) / exp(-x**3)
]
