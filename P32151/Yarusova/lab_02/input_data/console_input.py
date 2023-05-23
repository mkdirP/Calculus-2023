# choose the interval
def choose_interval():
    a = float(input("Enter the left border of the interval: "))
    b = float(input("Enter the right border of the interval: "))
    return a, b


# choose the accuracy
def choose_accuracy():
    accuracy = float(input("Enter the accuracy: "))
    return accuracy


def choose_max_iterations():
    max_iterations = int(input("Enter the max iterations: "))
    return max_iterations


def choose_initial_approximation():
    x0 = float(input("Enter the initial approximation for x: "))
    y0 = float(input("Enter the initial approximation for y: "))
    return x0, y0
