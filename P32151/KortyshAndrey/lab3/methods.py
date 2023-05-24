import sympy
from sympy import Symbol, Add, lambdify
from typing import Tuple, List, Callable


def check_finish(k: int, integral0: float, integral1: float, eps: float) -> bool:
    return abs(integral1 - integral0) / (2**k-1) < eps


def generate_common_function_values(a: float, b: float, n: int, callable_function: Callable[[float], float], a_critical: bool, b_critical: bool, eps: float) -> List[float]:
    points = [a + (b - a) / n * i for i in range(n + 1)]
    if a_critical:
        points[0] += eps / 1000
    if b_critical:
        points[-1] -= eps / 1000
    function_values = [callable_function(i) for i in points]
    return function_values


def abstract_method(n: int, eps: float, func: Add, a: float, b: float,
                    iteration_function: Callable[[int, float, float, Callable[[float], float], bool, bool, float], float],
                    k: int, critical_points: List[Tuple[float, bool, bool]]) -> Tuple[bool, int, float]:

    a_critical = False
    b_critical = False
    for point, converges_left, converges_right in critical_points:
        if point == a:
            a_critical = True
            if not converges_right:
                return False, -1, -1
        if point == b:
            b_critical = True
            if not converges_left:
                return False, -1, -1
        if a < point < b:
            result1 = abstract_method(n, eps, func, a, point, iteration_function, k, critical_points)
            result2 = abstract_method(n, eps, func, point, b, iteration_function, k, critical_points)
            return result1[0] and result2[0], result1[1] + result2[1], result1[2] + result2[2]

    callable_function: Callable[[float], float] = lambdify(x, func, "numpy")

    prev_ans = -1e9
    cur_ans = 1e9
    while not check_finish(k, prev_ans, cur_ans, eps):
        prev_ans, cur_ans = iteration_function(n, a, b, callable_function, a_critical, b_critical, eps),\
                            iteration_function(2 * n, a, b, callable_function, a_critical, b_critical, eps)
        n *= 2
    return True, n, cur_ans


def right_rectangle_method(n: int, eps: float, func: Add, a: float, b: float, critical_points: List[Tuple[float, bool, bool]]) -> Tuple[bool, int, float]:

    def iteration_function(n: int, a: float, b: float, callable_function: Callable[[float], float], a_critical: bool, b_critical: bool, eps: float) -> float:
        function_values = generate_common_function_values(a, b, n, callable_function, a_critical, b_critical, eps)
        return (b-a)/n * sum(i for i in function_values[1:])

    return abstract_method(n, eps, func, a, b, iteration_function, 2, critical_points)


def left_rectangle_method(n: int, eps: float, func: Add, a: float, b: float, critical_points: List[Tuple[float, bool, bool]]) -> Tuple[bool, int, float]:

    def iteration_function(n: int, a: float, b: float, callable_function: Callable[[float], float], a_critical: bool, b_critical: bool, eps: float) -> float:
        function_values = generate_common_function_values(a, b, n, callable_function, a_critical, b_critical, eps)
        return (b - a) / n * sum(i for i in function_values[:-1])

    return abstract_method(n, eps, func, a, b, iteration_function, 2, critical_points)


def middle_rectangle_method(n: int, eps: float, func: Add, a: float, b: float, critical_points: List[Tuple[float, bool, bool]]) -> Tuple[bool, int, float]:

    def iteration_function(n: int, a: float, b: float, callable_function: Callable[[float], float], a_critical: bool, b_critical: bool, eps: float) -> float:
        points = [a + (b - a) / n * i + (b - a) / (2*n) for i in range(n + 1)]
        function_values = [callable_function(i) for i in points]
        return (b - a) / n * sum(i for i in function_values[:-1])

    return abstract_method(n, eps, func, a, b, iteration_function, 2, critical_points)


def trapezoid_method(n: int, eps: float, func: Add, a: float, b: float, critical_points: List[Tuple[float, bool, bool]]) -> Tuple[bool, int, float]:

    def iteration_function(n: int, a: float, b: float, callable_function: Callable[[float], float], a_critical: bool, b_critical: bool, eps: float) -> float:
        function_values = generate_common_function_values(a, b, n, callable_function, a_critical, b_critical, eps)
        return (b - a) / n * ((function_values[0] + function_values[-1]) / 2 + sum(function_values[1:-1]))

    return abstract_method(n, eps, func, a, b, iteration_function, 2, critical_points)


def simpson_method(n: int, eps: float, func: Add, a: float, b: float, critical_points: List[Tuple[float, bool, bool]]) -> Tuple[bool, int, float]:

    def iteration_function(n: int, a: float, b: float, callable_function: Callable[[float], float], a_critical: bool, b_critical: bool, eps: float) -> float:
        function_values = generate_common_function_values(a, b, n, callable_function, a_critical, b_critical, eps)
        return (b - a) / (3*n) * (function_values[0] + function_values[-1] + 4 * sum(function_values[1:-1:2]) + 2 * sum(function_values[2:-1:2]))

    return abstract_method(n, eps, func, a, b, iteration_function, 4, critical_points)


x = Symbol("x")
methods: List[Callable[[int, float, Add, float, float, List[Tuple[float, bool, bool]]], Tuple[bool, int, float]]] = [
    right_rectangle_method,
    left_rectangle_method,
    middle_rectangle_method,
    trapezoid_method,
    simpson_method
]
method_names: List[str] = [
    "Метод правых прямоугольников",
    "Метод левых прямоугольников",
    "Метод средних прямоугольников",
    "Метод трапеций",
    "Метод Симпсона"
]
functions: List[Add] = [
    -2 * x ** 3 - 3 * x ** 2 + x + 5,
    1/x**.5,
    1/(1-x),
    sympy.E**(2*x),
    sympy.sin(x)/(sympy.cos(x)**2+1)
]
# For each function we precalculate the list of critical points
# For each critical point we store tuple of (point, limit converges from left, limit converges from right)
function_critical_points: List[List[Tuple[float, bool, bool]]] = [
    [],
    [(0, True, True)],
    [(1, False, False)],
    [],
    []
]
