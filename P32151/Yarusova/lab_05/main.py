from get_data import get_data
import methods
from util import plot_result
from util import plot_both_results


data, method, interpolation_dot = get_data()
if data is None or method is None or interpolation_dot is None:
    print("Wrong data")
    exit(0)
match method:
    case 1:
        result_lagrange = methods.lagrange(data, interpolation_dot)
        print(f"Result by Lagrange: {result_lagrange}")
        plot_result(data, interpolation_dot, result_lagrange)
    case 2:
        result_newton = methods.newton(data, interpolation_dot, True)
        print(f"Result by Newton: {result_newton}")
        for dot in data['x']:
            result_newton_dots = methods.newton(data, dot)
        plot_result(data, interpolation_dot, result_newton, result_newton_dots)
    case 3:
        result_lagrange = methods.lagrange(data, interpolation_dot)
        result_newton = methods.newton(data, interpolation_dot, True)
        print(f"Result by Lagrange: {result_lagrange}")
        print(f"Result by Newton: {result_newton}")
        result_newton_dots = []
        for dot in data['x']:
            result_newton_dots.append(methods.newton(data, dot))
        plot_both_results(data, interpolation_dot, result_lagrange, result_newton_dots)
