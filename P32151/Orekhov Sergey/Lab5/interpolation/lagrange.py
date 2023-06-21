from interpolation.universal import *


def lagrange_function(x, X, Y):
    n = len(X)
    L_sum = 0
    for i in range(n):
        l_i = 1
        for j in range(n):
            if j == i:
                continue
            l_i *= ((x - X[j])/(X[i] - X[j]))
        l_i *= Y[i]
        L_sum += l_i
    return L_sum
