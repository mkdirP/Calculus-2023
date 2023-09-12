# Description: This module contains the function to get the user input
import math


# choose the equation
def choose_equation():
    print("Choose the equation:")
    print("1. x^3 - 3x^2 + 2 = 0 (default)")
    print("2. x - cos(x) = 0")
    print("3. x^3 - 2x^2 - 5x + 6 = 0")
    print("4. 2,3x^3 + 5,75x^2 - 7,41x - 10,6 = 0")
    print("5. x^2 - 2x - 3 = 0")
    equation = int(input())
    match equation:
        case 1:
            return lambda x: x ** 3 - 3 * x ** 2 + 2
        case 2:
            return lambda x: x - math.cos(x)
        case 3:
            return lambda x: x ** 3 - 2 * x ** 2 - 5 * x + 6
        case 4:
            return lambda x: 2.3 * x ** 3 + 5.75 * x ** 2 - 7.41 * x - 10.6
        case 5:
            return lambda x: x ** 2 - 2 * x - 3
        case _:
            return lambda x: x ** 3 - 3 * x ** 2 + 2


# choose the equations
def choose_equations():
    print("Choose the system of equations:")
    print("1. {x^2 + y^2 = 4; y = 3x^2} (default)")
    print("2. {0,1x^2 + x + 0,2y^2 = 0,3; 0,2x^2 + y + 0,1xy = 0,7}")
    equation = int(input())
    match equation:
        case 1:
            return 1, 2
        case 2:
            return 3, 4
        case _:
            return 1, 2


# choose the method
def choose_method():
    print("Choose the method:")
    print("1. Chord method (default)")
    print("2. Secant method")
    print("3. Simple iteration method")
    print("4. Simple iteration method for systems")
    method = int(input())
    if method is None or method > 4 or method < 1:
        method = 1
    return method


# choose input format
def choose_input_format():
    print("Choose the input format:")
    print("1. Console (default)")
    print("2. File")
    input_format = int(input())
    return input_format


# choose the output format
def choose_output_format():
    print("Choose the output format:")
    print("1. Console (default)")
    print("2. File")
    output_format = int(input())
    return output_format


def validate_interval(a, b):
    if a > b:
        a, b = b, a
    return a, b
