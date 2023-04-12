from typing import List, Tuple, Callable
from sympy import Symbol, Add, lambdify


var = Symbol('var')


def determinant(matrix: List[List[float]]) -> float:
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    ans = 0
    for index, element in enumerate(matrix[0]):
        new_matrix = [[el for index_col, el in enumerate(row) if index_row != index and index_col != index]
                      for index_row, row in enumerate(matrix)]
        ans += determinant(new_matrix) * (-element if index % 2 else element)
    return ans


def get_linear(x: List[float], y: List[float]) -> Tuple[Add, float]:
    SXX = sum(i*i for i in x)
    SX = sum(x)
    SXY = sum(i*j for i, j in zip(x, y))
    SY = sum(y)
    det = determinant([[SXX, SX], [SX, len(x)]])
    det1 = determinant([[SXY, SX], [SY, len(x)]])
    det2 = determinant([[SXX, SXY], [SX, SY]])
    a = det1 / det
    b = det2 / det
    func: Add = a*var + b
    return func, get_standard_deviation(func, x, y)


def get_standard_deviation(func: Add, x: List[float], y: List[float]) -> float:
    callable_function: Callable[[float], float] = lambdify(var, func, "numpy")
    return sum((callable_function(x_i) - y_i) ** 2 for x_i, y_i in zip(x, y)) / len(x)
