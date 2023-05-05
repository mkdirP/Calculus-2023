from typing import List, Tuple
from sympy import Add, Symbol, lambdify

var = Symbol("x")


def get_finite_differences(x: List[float], y: List[float]) -> List[List[float]]:
    differences = [[y[i]] for i in range(len(x))]
    for col in range(1, len(x)):
        for row in range(len(x)):
            if col + row == len(x):
                break
            differences[row].append(differences[row+1][col-1] - differences[row][col-1])
    return differences


def get_lagrange_polynom(x: List[float], y: List[float], x_ans: float) -> Tuple[Add, float]:
    lagrange_polynom: Add = Add(0)
    for i in range(len(x)):
        cur_term: Add = Add(y[i])
        for j in range(len(x)):
            if i != j:
                cur_term *= (var - x[j]) / (x[i] - x[j])
        lagrange_polynom += cur_term
    callable_lagrange_polynom = lambdify(var, lagrange_polynom, "numpy")
    return lagrange_polynom, callable_lagrange_polynom(x_ans)


def check_algebraic_progression(x: List[float], possible_delta=1e6):
    diff = x[1] - x[0]
    for index, el in enumerate(x):
        if abs(x[0] + index * diff - el) > possible_delta:
            raise ValueError


def get_gauss_polynom(x: List[float], y: List[float], x_ans: float) -> Tuple[Add, float]:

    # Check that there is h
    check_algebraic_progression(x)

    # make sure that number of points is odd
    cur_x = x[::]
    cur_y = y[::]
    if len(cur_x) % 2 == 0:
        cur_x = cur_x[:-1]
        cur_y = cur_y[:-1]

    differences = get_finite_differences(cur_x, cur_y)
    middle = len(cur_x) // 2  # cur_x[middle] = x_0 in terms of lecture
    h = cur_x[1] - cur_x[0]
    t = (var - cur_x[middle]) / h
    gauss_polynom = Add(cur_y[middle])
    first_formula_fl = x_ans > cur_x[middle]
    addition = 0
    cur_term = 1
    for i in range(1, len(cur_x)):
        if i % 2 == 0:
            addition += 1
        if first_formula_fl:
            if i % 2 == 0:
                cur_term *= (t - addition)
            else:
                cur_term *= (t + addition)
        else:
            if i % 2 == 0:
                cur_term *= (t + addition)
            else:
                cur_term *= (t - addition)
        cur_term /= i
        cur_delta = differences[middle - i // 2][i] if first_formula_fl else differences[middle - (i + 1) // 2][i]
        gauss_polynom += cur_delta * cur_term
    callable_gauss_polynom = lambdify(var, gauss_polynom, "numpy")
    return gauss_polynom, callable_gauss_polynom(x_ans)
