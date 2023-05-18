from math import log, exp
from approximation import line
import tools

def logarithm(dots):
    n = len(dots)
    if not all([dot[1] >= 0 for dot in dots]):
        return None
    x = [dot[0] for dot in dots]
    y = [dot[1] for dot in dots]
    ln_x = [log(jx) for jx in x]
    result_ln = line([(ln_x[i], y[i]) for i in range(n)])
    a = result_ln['a']
    b = result_ln['b']
    result = {'a': a, 'b': b}
    f = lambda k: a * log(k) + b
    result['f'] = f
    result['string_f'] = f'y = {round(a, 3)}ln(x) + {round(b, 3)}'
    result['x'] = x
    result['y'] = y
    result['f(x)'] = [f(x[i]) for i in range(n)]
    result['variance'] = tools.variance(dots, f)
    result['standard_deviation'] = tools.standard_deviation(result['variance'])
    return result
