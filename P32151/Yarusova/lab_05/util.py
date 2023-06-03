import matplotlib.pyplot as plt
import methods


def plot_result(data, interpolation_dot, result, newton_dots = None):
    plt.plot(data['x'], data['y'], marker=".", label='Input dots')
    if newton_dots is not None:
        plt.plot(data['x'], newton_dots, marker="o", label='Newton dots')
    else:
        plt.plot([interpolation_dot], [result], marker="o", label='Interpolation result')
    # legend in left upper corner
    plt.legend(loc='upper left')
    plt.show()


def plot_both_results(data, interpolation_dot, result_lagrange, newton_dots = None):
    plt.plot(data['x'], data['y'], marker=".", label='Input dots')
    if newton_dots is not None:
        plt.plot(data['x'], newton_dots, marker="o", label='Newton dots')
    plt.plot(interpolation_dot, result_lagrange, 'o', label='Interpolation result by Lagrange')
    # legend in left upper corner
    plt.legend(loc='upper left')
    plt.show()
