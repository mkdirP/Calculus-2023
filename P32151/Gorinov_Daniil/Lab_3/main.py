def rectangle_method(f, a, b, e, min_n=4, max_itr=10):
    n = min_n
    result = float('inf')
    while n <= n * (2 ** max_itr):
        last_result = result
        result = 0
        h = (b - a) / n
        x = a
        for _ in range(n):
            result += f(x + h / 2)
            x += h
        result *= h
        if abs(result - last_result) <= e:
            break
        else:
            n *= 2
    return {'result': result, 'n': n}


def trapezoid_method(f, a, b, e, min_n=4, max_itr=10):
    n = min_n
    result = float('inf')
    while n <= n * (2 ** max_itr):
        last_result = result
        result = (f(a) + f(b)) / 2
        h = (b - a) / n
        x = a + h

        for _ in range(n - 1):
            result += f(x)
            x += h
        result *= h

        if abs(result - last_result) <= e:
            break
        else:
            n *= 2
    return {'result': result, 'n': n}


def simpson_method(f, a, b, e, min_n=4, max_itr=10):
    if min_n % 2 != 0:
        return None
    n = min_n
    result = float('inf')
    while n <= n * (2 ** max_itr):
        last_result = result
        result = f(a) + f(b)
        h = (b - a) / n
        x = a + h

        for i in range(n - 1):
            coeff = 4 if i % 2 == 0 else 2
            result += coeff * f(x)
            x += h
        result *= h / 3

        if abs(result - last_result) <= e:
            break
        else:
            n *= 2
    return {'result': result, 'n': n}


def death_dot(f, a, b, e, x0):
    answer1 = rectangle_method(f, a, x0 - e, e)
    answer2 = rectangle_method(f, x0 + e, b, e)
    data = {
        'result': answer1['result'] + answer2['result'],
        'n': answer1['n'] + answer2['n']
    }
    return data


def getfunc(func_id):
    functions = {
        '1': lambda x: x ** 2,
        '2': lambda x: 1 / x,
        '3': lambda x: (-x) ** 3 - (x ** 2) + x + 3
    }
    return functions.get(func_id)


def getmethod(method_id):
    methods = {
        '1': rectangle_method,
        '2': trapezoid_method,
        '3': simpson_method,
        '4': death_dot
    }
    return methods.get(method_id)


def getdata_input():
    data = {}

    print("\nВыберите функцию.")
    print(" 1 — x²")
    print(" 2 — 1/x")
    print(" 3 — -x³-x²+x+3")
    while True:
        try:
            func_id = input("Функция: ")
            func = getfunc(func_id)
            if func is None:
                raise AttributeError
            break
        except AttributeError:
            print("Функции нет в списке.")
    data['func'] = func

    print("\nВыберите метод решения.")
    print(" 1 — Метод прямоугольников")
    print(" 2 — Метод трапеций")
    print(" 3 — Метод Симпсона")
    print(" 4 — РАЗРЫВ X0 = 0")
    while True:
        try:
            method_id = input("Метод решения: ")
            method = getmethod(method_id)
            if method is None:
                raise AttributeError
            break
        except AttributeError:
            print("Метода нет в списке.")
    data['method'] = method

    print("\nВведите пределы интегрирования.")
    while True:
        try:
            a, b = map(float, input("Пределы интегрирования: ").split())
            a, b = sorted([a, b])
            break
        except ValueError:
            print("Пределы интегрирования должны быть числами, введенными через пробел.")
    data['a'] = a
    data['b'] = b

    print("\nВведите погрешность вычисления.")
    while True:
        try:
            error = float(input("Погрешность вычисления: "))
            if error <= 0:
                raise ArithmeticError
            break
        except (ValueError, ArithmeticError):
            print("Погрешность вычисления должна быть положительным числом.")
    data['error'] = error

    return data


if __name__ == '__main__':
    print("\033[93m{}\033[0m".format("Лабораторная работа #3\n"
                                     "Горинов Даниил Андреевич\n"
                                     "Вариант 3"))
    data = getdata_input()
    method = data['method']
    answer = method(data['func'], data['a'], data['b'], data['error'], 0) if method == getmethod("4") else method(data['func'], data['a'], data['b'], data['error'])
    print("\n\nРезультаты вычисления.")
    if answer:
        print(f"Значение интеграла: {answer['result']}")
        print(f"Количество разбиений: {answer['n']}")
    else:
        print("Ошибка при выполнении вычислений.")
