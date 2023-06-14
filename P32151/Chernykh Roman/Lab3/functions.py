def get_function(num):
    if num == 1:
        return lambda x: x ** 3 - 3 * x ** 2 + 7 * x - 10
    if num == 2:
        return lambda x: x ** 2 + 3 * x - 7
    if num == 3:
        return lambda x: 6 * x - 18


def get_function_name(num):
    if num == 1:
        return "x^3 - 3x^2 + 7x - 10"
    if num == 2:
        return "x^2 + 3x - 7"
    if num == 3:
        return "6x - 18"
