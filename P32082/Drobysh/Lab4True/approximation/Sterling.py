def delta(power, i, Y):
    if i < 0:
        return 0
    if power == 1:
        return Y[i + 1] - Y[i]
    else:
        return delta(power - 1, i + 1, Y) - delta(power - 1, i, Y)


def stirling(x, h, Y, X):
    t = (x - X[0])/h

