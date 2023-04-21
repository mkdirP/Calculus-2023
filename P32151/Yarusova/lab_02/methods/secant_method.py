from scipy.misc import derivative


def secant_method(f, a, b, accuracy, max_iterations):
    if f(a) * derivative(f, a, dx=0.01, n=2) > 0:
        x_prev = a
    else:
        x_prev = b
    iterations = 0
    x = x_prev - f(x_prev) / derivative(f, x_prev, dx=0.01, n=1)
    while (iterations < max_iterations) and (abs(f(x)) > accuracy) and (abs(x_prev - x) > accuracy):
        iterations += 1
        buf = x
        x = x - f(x) * (x - x_prev) / (f(x) - f(x_prev))
        x_prev = buf
    return x, iterations
