from InputCorrect import InputCorrect
from Integral import Integral
from IntegralMethod import IntegralMethod


class FunctionIntegralSolver:
    """
    Класс для решения определенных интегралов различных функций.
    """

    def __init__(self):
        """
        Инициализирует объект FunctionIntegralSolver.
        """
        self.variants = [
            "-3x^3 - 5x^2 + 4x - 2",
            "x^2 + x + 2",
            "3x^2 - 14x - 5",
            "x^2 + 2x + 1"
        ]
        self.values = [
            Integral(lambda x: - 3 * x ** 3 - 5 * x ** 2 + 4 * x - 2),
            Integral(lambda x: x ** 2 + x + 2),
            Integral(lambda x: 3 * x ** 2 - 14 * x - 5),
            Integral(lambda x: x ** 2 + 2 * x + 1)
        ]
        self.selected_function = None

    def select_function(self):
        """
        Позволяет пользователю выбрать функцию для интегрирования.
        """
        self.selected_function = InputCorrect.get_multiple_choice_input(
            self.variants, self.values, "Выберите функцию для интегрирования:")

    def solve_integral(self):
        """
        Решает определенный интеграл выбранной функции с использованием выбранного метода интегрирования.
        """
        variants = [
            "Метод прямоугольника - левый",
            "Метод прямоугольника - центр",
            "Метод прямоугольника - правый",
            "Метод трапеций",
            "Метод Симпсона"
        ]
        values = [
            IntegralMethod.left_rectangle,
            IntegralMethod.center_rectangle,
            IntegralMethod.right_rectangle,
            IntegralMethod.trapezoid_method,
            IntegralMethod.simpson_method
        ]
        selected_method = InputCorrect.get_multiple_choice_input(variants, values, "Выберите метод интегрирования:")

        left_limit = InputCorrect.get_float_input("Введите левый предел интегрирования: ")
        right_limit = InputCorrect.get_float_input("Введите правый предел интегрирования: ")
        while not left_limit < right_limit:
            print("Левый предел должен быть меньше правого.")
            left_limit = InputCorrect.get_float_input("Введите левый предел интегрирования: ")
            right_limit = InputCorrect.get_float_input("Введите правый предел интегрирования: ")

        try:
            result = self.selected_function.solve(left_limit, right_limit, selected_method)
            if result is not None:
                print("Результат вычисления:", result)
                print("Число разбиений:", self.selected_function.steps)
                if InputCorrect.get_yes_or_no_input("Нарисовать график функции?"):
                    self.selected_function.draw_function(left_limit, right_limit)
            else:
                print("На заданном промежутке интеграл не существует.")
        except Exception:
            print("Не удалось найти значение интеграла.\n"
                  "Попробуйте ввести другие пределы интегрирования.")
