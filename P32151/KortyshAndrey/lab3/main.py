from methods import functions, method_names, methods
from typing import Callable, Tuple
from sympy import Add


def get_method(index: int) -> Callable[[int, float, Add, float, float], Tuple[int, float]]:
    if index < 0 or index > len(methods) - 1:
        raise ValueError
    return methods[index]


def get_function(index: int) -> Add:
    if index < 0 or index > len(functions) - 1:
        raise ValueError
    return functions[index]


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


def print_results(results: Tuple[int, float], eps: float) -> None:
    print(f"Итоговое число разбиений: {results[0]}")
    print(f"Значение интеграла: {round(results[1], get_error_length(eps))}")


def main():
    try:
        print("Введите номер функции")
        print_functions()
        function_number = int(input())
        func = get_function(function_number - 1)
        print("Введите номер метода")
        print_methods()
        method_number = int(input())
        method = get_method(method_number - 1)
        a, b = map(float, input("Введите границы интегрирования через пробел, например, 2.44 14.1: ").split())
        if b < a:
            raise ValueError
        eps = float(input("Введите погрешность вычисления: "))
        print_results(method(4, eps, func, a, b), eps)
    except ValueError:
        print("Неверное значение")


if __name__ == "__main__":
    main()
