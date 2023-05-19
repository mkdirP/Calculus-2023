from io import get_data

data, method, interpolation_dot = get_data()
if data is None or method is None or interpolation_dot is None:
    print("Wrong data")
    exit(0)
match method:
    case 1:
        result = lagrange(data, interpolation_dot)
    case 2:
        result = newton(data, interpolation_dot)
    case 3:
        result_lagrange = lagrange(data, interpolation_dot)
        result_newton = newton(data, interpolation_dot)
