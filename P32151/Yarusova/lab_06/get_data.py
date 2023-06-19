from math import exp, cos, sin


def get_data():
    equation, equation_num = choose_equation()
    x0, xn = choose_interval()
    y0 = choose_y0()
    h = choose_h()
    accuracy = choose_accuracy()
    result_equation = find_result_equation(equation_num, x0, y0)
    return equation, result_equation, x0, xn, y0, h, accuracy


def choose_equation():
    print("Choose the equation:")
    print("1. y' = 2x (default)")
    print("2. y' = e^(-3x)")
    print("3. y' = cos(x)")
    equation = int(input())
    if equation not in [1, 2, 3]:
        print("Wrong equation (default))")
        equation = 1
    func = lambda x, y: 2 * x
    match equation:
        case 2:
            func = lambda x, y: exp(-3 * x)
        case 3:
            func = lambda x, y: cos(x)
    return func, equation


def choose_interval():
    print("Enter interval: ")
    print("Enter left border x0 (default 0): ")
    left = float(input())
    print("Enter right border xn (default 1): ")
    right = float(input())
    if left is None:
        left = 0
    if right is None:
        right = 1
    if left == right:
        print("Left and right borders must be different (default)")
        left, right = 0, 1
    if left > right:
        print("Left border must be less than right border(swap them)")
        left, right = right, left
    return left, right


def choose_y0():
    print("Enter y(x0) (default 0): ")
    y_0 = float(input())
    if y_0 is None:
        y_0 = 0
    return y_0


def choose_h():
    print("Enter h (default 0.1): ")
    h = float(input())
    if h is None or h <= 0:
        print("h must be positive(default)")
        h = 0.1
    return h


def choose_accuracy():
    print("Enter accuracy (default 0.01): ")
    accuracy = float(input())
    if accuracy is None or accuracy <= 0:
        print("Accuracy must be positive(default)")
        accuracy = 0.01
    return accuracy


def find_result_equation(equation, x0, y0):
    if equation == 1:
        return lambda x: x ** 2 + y0 - x0 ** 2
    if equation == 2:
        return lambda x: -1 / 3 * exp(-3 * x) + y0 + 1 / 3 * exp(-3 * x0)
    if equation == 3:
        return lambda x: sin(x) + y0 - sin(x0)
    print("Wrong equation (default)")
    return lambda x: x ** 2 + y0 - x0 ** 2
