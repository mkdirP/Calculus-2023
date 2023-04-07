from methods import functions, method_names, methods, function_critical_points
from typing import Callable, Tuple, List
from sympy import Add


def get_method(index: int) -> Callable[[int, float, Add, float, float, List[Tuple[float, bool, bool]]], Tuple[bool, int, float]]:
    if index < 0 or index > len(methods) - 1:
        raise ValueError
    return methods[index]


def get_function(index: int) -> Tuple[Add, List[Tuple[float, bool, bool]]]:
    if index < 0 or index > len(functions) - 1:
        raise ValueError
    return functions[index], function_critical_points[index]


def print_functions() -> None:
    for index, func in enumerate(functions):
        print(f"{index+1}. {func}")


def print_methods() -> None:
    for index, method in enumerate(method_names):
        print(f"{index+1}. {method}")


def get_error_length(eps: float) -> int:
    if "." in str(eps):
        return len(str(eps).split(".")[1])
    return abs(int(str(eps).split("e")[1]))


def print_results(results: Tuple[bool, int, float], eps: float) -> None:
    if not results[0]:
        print("Интеграл расходится.")
        return
    print(f"Итоговое число разбиений: {results[1]}")
    print(f"Значение интеграла: {round(results[2], get_error_length(eps))}")


def main():
    try:
        print("Введите номер функции")
        print_functions()
        function_number = int(input())
        func, critical_points = get_function(function_number - 1)
        print("Введите номер метода")
        print_methods()
        method_number = int(input())
        method = get_method(method_number - 1)
        a, b = map(float, input("Введите границы интегрирования через пробел, например, 2.44 14.1: ").split())
        if b < a:
            raise ValueError
        eps = float(input("Введите погрешность вычисления: "))
        print_results(method(4, eps, func, a, b, critical_points), eps)
    except ValueError:
        print("Неверное значение")


if __name__ == "__main__":
    main()
