def chord_method(equation, a, b, accuracy, max_iterations):
    iterations = 0
    x = (a * equation(b) - b * equation(a)) / (equation(b) - equation(a))
    prev = a
    while (iterations < max_iterations) and (abs(equation(x)) > accuracy) and (abs(b - a) > accuracy) and (abs(x - prev) > accuracy):
        iterations += 1
        if equation(a) * equation(x) < 0:
            b = x
        else:
            a = x
        prev = x
        x = (a * equation(b) - b * equation(a)) / (equation(b) - equation(a))
    return x, iterations
