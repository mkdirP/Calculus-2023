import numpy as np

from InputCorrect import InputCorrect
from MethodEquation import MethodEquation
from MethodSystem import MethodSystem


class VariantsFunctionSolver:
    """
    Класс для решения уравнений с заданными вариантами функций.
    """

    def __init__(self):
        self.equation_variants = [
            "x^3 - 4.5x^2 - 9.21x - 0.383",
            "x^3 - x + 4",
            "sin(x) + 0.1"
        ]
        self.equation_values = [
            MethodEquation(lambda x: x ** 3 - 4.5 * x ** 2 - 9.21 * x - 0.383,
                           derivative_func=lambda x: 3 * x ** 2 - 9 * x - 9.21),
            MethodEquation(lambda x: x ** 3 - x + 4, derivative_func=lambda x: 3 * x ** 2 - 1),
            MethodEquation(lambda x: np.sin(x) + 0.1, derivative_func=lambda x: np.cos(x))
        ]

    def solve(self):
        """
        Решает выбранное уравнение и выводит результаты.
        """
        chosen_equation = InputCorrect.get_multiple_choice_input(
            self.equation_variants, self.equation_values, "Выберите функцию:"
        )

        try:
            result = chosen_equation.solve()
        except ValueError:
            print("Возможно, функция не определена в некоторых точках.\n"
                  "Попробуйте ввести другие концы отрезка.")
            return

        if result is None:
            print("Не удалось найти корень уравнения.")
        else:
            print("Найденный корень уравнения:", round(result, 5))
            print("Значение функции в точке:", round(chosen_equation.calculate(result), 9))
            if InputCorrect.get_yes_or_no_input("Показать график функции?"):
                chosen_equation.draw_graphic(dot_x=result, dot_y=chosen_equation.calculate(result))


class SystemSolver:
    """
    Класс для решения системы уравнений с заданными вариантами.
    """

    def __init__(self):
        system1 = "┌ 0.1x^2 + x + 0.2y^2 - 0.3" + "\n" + \
                "   " + "└ 0.2x^2 + y + 0.1xy - 0.7"
        ms1 = MethodSystem(
            [lambda x, y: 0.1 * x ** 2 + x + 0.2 * y ** 2 - 0.3, lambda x, y: 0.2 * x ** 2 + y + 0.1 * x * y - 0.7],
            derivative_funcs=[lambda x, y: np.array([-0.2 * x, -0.4 * y]),
                              lambda x, y: np.array([-0.4 * x - 0.1 * y, -0.1 * x])]
        )
        system2 = "┌ sin(x)" + "\n" + \
                "   " + "└ xy/20 - 0.5"
        ms2 = MethodSystem(
            [lambda x, y: np.sin(x), lambda x, y: x * y / 20 - 0.5],
            derivative_funcs=[lambda x, y: np.array([np.cos(x), 0]),
                              lambda x, y: np.array([y / 20, x / 20])]
        )
        self.system_variants = [system1, system2]
        self.system_values = [ms1, ms2]

    def solve(self):
        """
        Решает выбранную систему уравнений и выводит результаты.
        """
        chosen_system = InputCorrect.get_multiple_choice_input(
            self.system_variants, self.system_values, "Выберите систему:"
        )

        result = chosen_system.solve()
        if result is None:
            print("Не удалось найти корень системы.")
        else:
            print("Найденный корень системы:", result)
            print("Значение системы в этой точке:", chosen_system.calculate(*result))
            print("Количество итераций:", chosen_system.iterations)
            print("Вектор погрешностей:", chosen_system.get_error_rate())
