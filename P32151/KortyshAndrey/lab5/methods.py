from typing import List, Tuple
from sympy import Add, Symbol, lambdify, sin

var = Symbol("x")


def get_finite_differences(y: List[float]) -> List[List[float]]:
    differences = [[y[i]] for i in range(len(y))]
    for col in range(1, len(y)):
        for row in range(len(y)):
            if col + row == len(y):
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

    first_formula_fl = x_ans > cur_x[len(cur_x) // 2]
    gauss_polynom = get_gauss(cur_x, cur_y, first_formula_fl)
    callable_gauss_polynom = lambdify(var, gauss_polynom, "numpy")
    return gauss_polynom, callable_gauss_polynom(x_ans)


def get_gauss(x: List[float], y: List[float], greater: bool) -> Add:
    differences = get_finite_differences(y)
    middle = len(x) // 2  # cur_x[middle] = x_0 in terms of lecture
    h = x[1] - x[0]
    t = (var - x[middle]) / h
    gauss_polynom = Add(y[middle])
    addition = 0
    cur_term = 1
    for i in range(1, len(x)):
        if i % 2 == 0:
            addition += 1
        if not greater:
            if i % 2 == 0:
                cur_term *= (t + addition)
            else:
                cur_term *= (t - addition)
        else:
            if i % 2 == 0:
                cur_term *= (t - addition)
            else:
                cur_term *= (t + addition)
        cur_term /= i
        cur_delta = differences[middle - (i + 1) // 2][i] if not greater else differences[middle - i // 2][i]
        gauss_polynom += cur_delta * cur_term
    return gauss_polynom


def get_stirling_polynom(x: List[float], y: List[float], x_ans: float) -> Tuple[Add, float]:
    # Check that there is h
    check_algebraic_progression(x)

    # make sure that number of points is odd
    cur_x = x[::]
    cur_y = y[::]
    if len(cur_x) % 2 == 0:
        cur_x = cur_x[:-1]
        cur_y = cur_y[:-1]

    stirling_polynom = (get_gauss(cur_x, cur_y, True) + get_gauss(cur_x, cur_y, False)) / 2
    callable_stirling_polynom = lambdify(var, stirling_polynom, "numpy")
    return stirling_polynom, callable_stirling_polynom(x_ans)


def get_bessel_polynom(x: List[float], y: List[float], x_ans: float) -> Tuple[Add, float]:
    # Check that there is h
    check_algebraic_progression(x)

    # make sure that number of points is even
    cur_x = x[::]
    cur_y = y[::]
    if len(cur_x) % 2 == 1:
        cur_x = cur_x[:-1]
        cur_y = cur_y[:-1]

    cur_term = Add(1)
    h = cur_x[1] - cur_x[0]
    middle = len(cur_x) // 2 - 1
    t = (var - cur_x[middle]) / h
    diff = get_finite_differences(cur_y)
    bessel_polynom = Add(0)
    for i in range(len(cur_x)):
        if i != 0:
            cur_term /= i
        if i % 2 == 0:
            bessel_polynom += cur_term*(diff[middle - i//2][i] + diff[middle - i//2+1][i]) / 2
        else:
            bessel_polynom += cur_term*(t - 1/2)*diff[middle - i//2][i]
            cur_term *= (t - (i + 1) // 2)*(t + (i + 1) // 2 - 1)
    callable_bessel_polynom = lambdify(var, bessel_polynom, "numpy")
    return bessel_polynom, callable_bessel_polynom(x_ans)


functions = [
    sin(var),
    1 / (var ** 2 + 1)
]
