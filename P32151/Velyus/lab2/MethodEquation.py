import numpy as np
from matplotlib import pyplot as plt

from InputCorrect import InputCorrect


class MethodEquation:
    """
    Класс для решения уравнений различными численными методами.
    """

    def __init__(self, func, derivative_func=None):
        """
        Инициализация объекта MethodEquation.

        Args:
            func (function): Функция, для которой выполняется решение уравнения.
            derivative_func (function, optional): Производная функции. Defaults to None.
        """
        self.func = func
        self.derivative_func = derivative_func
        self.iterations = 0
        self.left = None
        self.right = None

    def calculate(self, argument):
        """
        Вычисляет значение функции в заданной точке.

        Args:
            argument: Аргумент функции.

        Returns:
            Значение функции в точке arg.
        """
        try:
            return self.func(argument)
        except Exception:
            raise ValueError

    def solve(self):
        """
        Запускает выбранный метод решения уравнения.

        Returns:
            float: Результат решения уравнения.
        """
        variants = ["Метод хорд", "Метод Ньютона", "Метод простых итераций"]
        values = [self.chord_method, self.newtons_method, self.simple_iteration_method]
        chosen_method = InputCorrect.get_multiple_choice_input(variants, values, "Выберите метод решения уравнения: ")
        return chosen_method()

    def _enter_root_isolation(self):
        """
        Запрашивает у пользователя интервал изоляции корня.

        Returns:
            tuple: Кортеж с левым и правым концами интервала изоляции.
        """
        print("Введите интервал изоляции корня:")
        left_cut = InputCorrect.get_float_input("\tЛевый конец отрезка: ")
        right_cut = InputCorrect.get_float_input("\tПравый конец отрезка: ")

        while not self.calculate(left_cut) * self.calculate(right_cut) < 0:
            print("Значения функции на концах отрезка должны быть разного знака!")
            if InputCorrect.get_yes_or_no_input(f"Показать график функции для корректировки?"):
                self.draw_graphic(left_cut, right_cut)
            print("Введите другие значения концов:")
            left_cut = InputCorrect.get_float_input("\tЛевый конец отрезка: ")
            right_cut = InputCorrect.get_float_input("\tПравый конец отрезка: ")
        if self.calculate(left_cut) > 0:
            left_cut, right_cut = right_cut, left_cut
        self.left, self.right = left_cut, right_cut
        return left_cut, right_cut

    def draw_graphic(self, left_cut=None, right_cut=None, dot_x=None, dot_y=None):
        """
        Выводит график функции.

        Args:
            left_cut (float, optional): Левый конец отрезка. Defaults to None.
            right_cut (float, optional): Правый конец отрезка. Defaults to None.
            dot_x (float, optional): Горизонтальная координата точки для выделения. Defaults to None.
            dot_y (float, optional): Вертикальная координата точки для выделения. Defaults to None.
        """
        if left_cut is None or right_cut is None:
            if self.left is None or self.right is None:
                print("Невозможно нарисовать график. Не определены концы отрезка")
            else:
                left_cut = self.left
                right_cut = self.right
        grid = abs(left_cut - right_cut) / 30
        x_axis = np.linspace(min(left_cut, right_cut) - grid, max(left_cut, right_cut) + grid, 32)
        plt.plot(x_axis, self.calculate(x_axis))
        plt.grid(True, which='both')
        if min(left_cut, right_cut) - grid <= 0 <= max(left_cut, right_cut) + grid:
            plt.axvline(x=0, color='k')
        plt.axhline(y=0, color='k')
        if dot_x is not None:
            if dot_y is None:
                dot_y = 0
            plt.plot(dot_x, dot_y, "ro")
        plt.show()

    def chord_method(self):
        """
        Решает уравнение методом хорд.

        Returns:
            float: Результат решения уравнения.
        """
        left_cut, right_cut = self._enter_root_isolation()

        epsilon = 10 ** (-8)
        x = left_cut - self.calculate(left_cut) * (right_cut - left_cut) / (self.calculate(right_cut) - self.calculate(left_cut))
        while abs(self.calculate(x)) > epsilon:
            x = left_cut - self.calculate(left_cut) * (right_cut - left_cut) / (self.calculate(right_cut) - self.calculate(left_cut))
            if self.calculate(x) > 0:
                right_cut = x
            else:
                left_cut = x
            self.iterations += 1

        return x

    def simple_iteration_method(self):
        """
        Решает уравнение методом простых итераций.

        Returns:
            float: Результат решения уравнения.
        """
        left_cut, right_cut = self._enter_root_isolation()
        hlife = -0.01 / max(abs(self.derivative_func(left_cut)), abs(self.derivative_func(right_cut)))
        phi = lambda x: x + hlife * self.calculate(x)
        print(f"Используемая лямбда={hlife}")

        epsilon = 10 ** (-8)
        x = InputCorrect.get_float_input("Введите начальное приближение: ")
        while not (min(left_cut, right_cut) < x < max(left_cut, right_cut)):
            x = InputCorrect.get_float_input("Введите начальное приближение внутри интервала изоляции корня: ")
        try:
            self.calculate(x)
        except Exception:
            print("Невозможно посчитать значение функции в заданной точке.")
            return None

        while abs(self.calculate(x)) > epsilon and self.iterations <= 1000000:
            x = phi(x)
            self.iterations += 1
        if self.iterations == 1000000:
            return None
        return x

    def newtons_method(self):
        """
        Решает уравнение методом Ньютона.

        Returns:
            float: Результат решения уравнения.
        """
        left_cut, right_cut = self._enter_root_isolation()
        x = InputCorrect.get_float_input("Введите начальное приближение: ")
        epsilon = 10 ** (-8)
        while abs(self.calculate(x)) > epsilon:
            x = x - self.calculate(x) / self.derivative_func(x)
            self.iterations += 1
        return x
