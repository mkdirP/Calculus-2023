from sympy import Symbol, Add, lambdify
from typing import Tuple, List, Callable


def check_finish(k: int, integral0: float, integral1: float, eps: float) -> bool:
    return abs(integral1 - integral0) / (2**k-1) < eps


def abstract_method(n: int, eps: float, func: Add, a: float, b: float,
                    iteration_function: Callable[[int, float, float, Callable[[float], float]], float], k: int) -> Tuple[int, float]:
    callable_function: Callable[[float], float] = lambdify(x, func, "numpy")
    prev_ans = -1e9
    cur_ans = 1e9
    while not check_finish(k, prev_ans, cur_ans, eps):
        prev_ans, cur_ans = iteration_function(n, a, b, callable_function), iteration_function(2 * n, a, b, callable_function)
        n *= 2
    return n, cur_ans


def right_rectangle_method(n: int, eps: float, func: Add, a: float, b: float) -> Tuple[int, float]:

    def iteration_function(n: int, a: float, b: float, callable_function: Callable[[float], float]) -> float:
        points = [a + (b-a)/n*i for i in range(n+1)]
        function_values = [callable_function(i) for i in points]
        return (b-a)/n * sum(i for i in function_values[1:])

    return abstract_method(n, eps, func, a, b, iteration_function, 2)


def left_rectangle_method(n: int, eps: float, func: Add, a: float, b: float) -> Tuple[int, float]:

    def iteration_function(n: int, a: float, b: float, callable_function: Callable[[float], float]) -> float:
        points = [a + (b - a) / n * i for i in range(n + 1)]
        function_values = [callable_function(i) for i in points]
        return (b - a) / n * sum(i for i in function_values[:-1])

    return abstract_method(n, eps, func, a, b, iteration_function, 2)


def middle_rectangle_method(n: int, eps: float, func: Add, a: float, b: float) -> Tuple[int, float]:

    def iteration_function(n: int, a: float, b: float, callable_function: Callable[[float], float]) -> float:
        points = [a + (b - a) / n * i + (b - a) / (2*n) for i in range(n + 1)]
        function_values = [callable_function(i) for i in points]
        return (b - a) / n * sum(i for i in function_values[:-1])

    return abstract_method(n, eps, func, a, b, iteration_function, 2)


def trapezoid_method(n: int, eps: float, func: Add, a: float, b: float) -> Tuple[int, float]:

    def iteration_function(n: int, a: float, b: float, callable_function: Callable[[float], float]) -> float:
        points = [a + (b - a) / n * i for i in range(n + 1)]
        function_values = [callable_function(i) for i in points]
        return (b - a) / n * ((function_values[0] + function_values[-1]) / 2 + sum(function_values[1:-1]))

    return abstract_method(n, eps, func, a, b, iteration_function, 2)


def simpson_method(n: int, eps: float, func: Add, a: float, b: float) -> Tuple[int, float]:

    def iteration_function(n: int, a: float, b: float, callable_function: Callable[[float], float]) -> float:
        points = [a + (b - a) / n * i for i in range(n + 1)]
        function_values = [callable_function(i) for i in points]
        return (b - a) / (3*n) * (function_values[0] + function_values[-1] + 4 * sum(function_values[1:-1:2]) + 2 * sum(function_values[2:-1:2]))

    return abstract_method(n, eps, func, a, b, iteration_function, 4)


x = Symbol("x")
methods: List[Callable[[int, float, Add, float, float], Tuple[int, float]]] = [
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

]
