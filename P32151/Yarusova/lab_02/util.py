from scipy.misc import derivative
import numpy as np
import matplotlib.pyplot as plt
from sympy import *


def check_for_roots(f, a, b):
    df_a = derivative(f, a, dx=0.01, n=1)
    if f(a) * f(b) < 0:
        for i in np.arange(a, b, 0.01):
            if df_a * derivative(f, i, dx=0.01, n=1) < 0:
                print("There are more than one root or no roots in the interval")
                return False
        return True
    print("There are more than one root or no roots in the interval")
    return False


# graphic
def draw_graphic(f, a, b, x):
    if x is None:
        print("Smth went wrong")
        return
    plt.plot([i for i in np.arange(a, b, 0.01)], [f(i) for i in np.arange(a, b, 0.01)])
    plt.plot(x, f(x), 'o')
    plt.show()


def draw_graphic_for_systems(f, g, a_1, b_1, a_2, b_2, x, y):
    if x is None or y is None:
        print("Smth went wrong")
        return
    q, w = symbols('q w')
    plot_1 = plot_implicit(Eq(f, 0), (q, a_1, b_1), (w, a_2, b_2), show=False)
    plot_2 = plot_implicit(Eq(g, 0), (q, a_1, b_1), (w, a_2, b_2), show=False)
    plot_1.append(plot_2[0])
    plot_1.show()
