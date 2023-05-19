from get_data import get_data
import methods

data, method, interpolation_dot = get_data()
if data is None or method is None or interpolation_dot is None:
    print("Wrong data")
    exit(0)
match method:
    case 1:
        result_lagrange = methods.lagrange(data, interpolation_dot)
        print(f"Result by Lagrange: {result_lagrange}")
    case 2:
        result_newton = methods.newton(data, interpolation_dot)
        print(f"Result by Newton: {result_newton}")
    case 3:
        result_lagrange = methods.lagrange(data, interpolation_dot)
        result_newton = methods.newton(data, interpolation_dot)
        print(f"Result by Lagrange: {result_lagrange}")
        print(f"Result by Newton: {result_newton}")
