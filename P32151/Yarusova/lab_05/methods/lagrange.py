
def lagrange(data, interpolation_dot):
    n = len(data['x'])
    result = 0
    for i in range(n):
        l = 1
        for j in range(n):
            if i != j:
                l *= (interpolation_dot - data['x'][j]) / (data['x'][i] - data['x'][j])
        result += l * data['y'][i]
    return result
