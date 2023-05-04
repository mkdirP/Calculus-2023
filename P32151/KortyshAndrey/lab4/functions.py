import math
from typing import List, Tuple, Callable
from sympy import Symbol, Add, lambdify
import sympy


var = Symbol('var')


def determinant(matrix: List[List[float]]) -> float:
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    ans = 0
    cur_row = 0
    for index, element in enumerate(matrix[cur_row]):
        new_matrix = [[el for index_col, el in enumerate(row) if index_col != index]
                      for index_row, row in enumerate(matrix) if index_row != cur_row]
        ans += determinant(new_matrix) * (-element if index % 2 else element)
    return ans


def get_polynom_coefficients(x: List[float], y: List[float], deg: int) -> List[float]:
    A = [[sum(x_i**(i+j) for x_i in x) for i in range(deg+1)] for j in range(deg+1)]
    B = [sum(x_i**i * y_i for x_i, y_i in zip(x, y)) for i in range(deg+1)]
    det = determinant(A)
    coefficients = []
    for i in range(deg+1):
        new_A = [[A[j][k] if k != i else B[j] for k in range(deg+1)] for j in range(deg+1)]
        cur_det = determinant(new_A)
        coefficients += [cur_det/det]
    return coefficients


def get_polynom(x: List[float], y: List[float], deg: int, precision: float) -> Tuple[Add, float]:
    func: Add = Add(0)
    for index, coef in enumerate(get_polynom_coefficients(x, y, deg)):
        func += (var**index)*round(coef, precision)
    return func, get_standard_deviation(func, x, y)


def get_exponential(x: List[float], y: List[float], precision: float) -> Tuple[Add, float]:
    lny = list(map(math.log, y))
    a, b = get_polynom_coefficients(x, lny, 1)
    func: Add = round(math.exp(a), precision)*sympy.exp(round(b, precision)*var)
    return func, get_standard_deviation(func, x, y)


def get_power(x: List[float], y: List[float], precision: float) -> Tuple[Add, float]:
    lnx = list(map(math.log, x))
    lny = list(map(math.log, y))
    a, b = get_polynom_coefficients(lnx, lny, 1)
    func: Add = round(math.exp(a), precision) * var**(round(b, precision))
    return func, get_standard_deviation(func, x, y)


def get_logarithmic(x: List[float], y: List[float], precision: float) -> Tuple[Add, float]:
    lnx = list(map(math.log, x))
    a, b = get_polynom_coefficients(lnx, y, 1)
    func: Add = round(b, precision)*sympy.ln(var) + round(a, precision)
    return func, get_standard_deviation(func, x, y)


def get_standard_deviation(func: Add, x: List[float], y: List[float]) -> float:
    callable_function: Callable[[float], float] = lambdify(var, func, "numpy")
    return (sum((callable_function(x_i) - y_i) ** 2 for x_i, y_i in zip(x, y)) / len(x)) ** .5


def get_extra_information(func: Add, x: List[float], y: List[float]) -> Tuple[List[float], List[float]]:
    callable_function = lambdify(var, func, "numpy")
    phi = [callable_function(x_i) for x_i in x]
    epsilon = [phi_i - y_i for phi_i, y_i in zip(phi, y)]
    return phi, epsilon


def get_pirson_coefficient(x: List[float], y: List[float]) -> float:
    mean_x = sum(x) / len(x)
    mean_y = sum(y) / len(y)
    return sum((x_i - mean_x)*(y_i - mean_y) for x_i, y_i in zip(x, y)) /\
           ((sum((x_i - mean_x)**2 for x_i in x)*sum((y_i - mean_y)**2 for y_i in y))**.5)
