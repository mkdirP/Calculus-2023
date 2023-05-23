# choose the interval
def choose_interval_from_file(f):
    a, b = float(f.readline().split())
    return a, b


# choose the accuracy
def choose_accuracy_from_file(f):
    accuracy = float(f.readline())
    return accuracy


def choose_initial_approximation_from_file(f):
    x0 = float(f.readline)
    y0 = float(f.readline)
    return x0, y0


def choose_max_iterations_from_file(f):
    max_iterations = int(f.readline())
    return max_iterations
