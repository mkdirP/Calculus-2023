import pandas as pd
from methods import *
from IO import *


def solution(f, x0, y0, h, xn, method, p, eps=None):
    df = pd.DataFrame(columns=["X", "Y original", "Y from method", "Runge Rule = Epsilon_mean", "Rate Runge Rule"])
    graph_f = f[1]
    f = f[0]

    # At first, we can find Y values from our method
    if eps is None:
        eps = 0.01
        X, Y_METHOD = method(f, x0, y0, h, xn)

        # Moving forward to calculating Runge Rule results (And rating them):

        r_result, rate = runge_rule(method, f, x0, y0, h, xn, p)

    else:
        X, Y_METHOD = method(f, x0, y0, h, xn, eps)

        # Moving forward to calculating Runge Rule results (And rating them):

        r_result, rate = runge_rule(method, f, x0, y0, h, xn, p, eps)

    # Now we need to find original Y values:
    Y_ORIGINAL = [f(x, f(x, x)) for x in X]

    df.loc[len(df)] = [x0, y0, y0, r_result, rate]

    for x, y_or, y_me in zip(X[1:], Y_ORIGINAL[1:], Y_METHOD[1:]):
        df.loc[len(df)] = [x, y_or, y_me, "-/-", "-/-"]

    # Finally, we will draw the graph and show the Data Frame:
    print(df)

    draw_graph_one_dot_one_function(graph_f, X, Y_METHOD)