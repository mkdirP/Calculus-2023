from typing import List, Tuple, Callable
from sympy import Symbol, Add, lambdify


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


def get_polynom(x: List[float], y: List[float], deg) -> Tuple[Add, float]:
    A = [[sum(x_i**(i+j) for x_i in x) for i in range(deg+1)] for j in range(deg+1)]
    B = [sum(x_i**i * y_i for x_i, y_i in zip(x, y)) for i in range(deg+1)]
    det = determinant(A)
    func: Add = Add(0)
    for i in range(deg+1):
        new_A = [[A[j][k] if k != i else B[j] for k in range(deg+1)] for j in range(deg+1)]
        cur_det = determinant(new_A)
        func += (var**i) * cur_det / det
    return func, get_standard_deviation(func, x, y)


def get_standard_deviation(func: Add, x: List[float], y: List[float]) -> float:
    callable_function: Callable[[float], float] = lambdify(var, func, "numpy")
    return sum((callable_function(x_i) - y_i) ** 2 for x_i, y_i in zip(x, y)) / len(x)
