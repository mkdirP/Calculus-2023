from math import log, exp
from approximation import line
import tools

def exponenta(dots):
    n = len(dots)
    if not all([dot[1] > 0 for dot in dots]):
        return None
    x = [dot[0] for dot in dots]
    y = [dot[1] for dot in dots]
    ln_y = [log(jy) for jy in y]
    result_ln = line([(x[i], ln_y[i]) for i in range(n)])
    a = exp(result_ln['b'])
    b = result_ln['a']
    result = {'a': a, 'b': b}
    f = lambda k: a * exp(b * k)
    result['f'] = f
    result['string_f'] = f'y = {round(a, 3)}e^{round(b, 3)}x'
    result['x'] = x
    result['y'] = y
    result['f(x)'] = [f(x[i]) for i in range(n)]
    result['variance'] = tools.variance(dots, f)
    result['standard_deviation'] = tools.standard_deviation(result['variance'])
    return result
