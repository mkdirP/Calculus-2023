import numpy as np
from matplotlib import cm
from matplotlib import pyplot as plt

from InputCorrect import InputCorrect


class MethodSystem:
    """
    Класс для решения системы уравнений методом простых итераций.

    Args:
        funcs (list): Список функций системы уравнений.
        derivative_funcs (list, optional): Список производных функций системы уравнений. Defaults to None.
    """

    def __init__(self, funcs, derivative_funcs=None):
        self.solutions = None
        self.funcs = funcs
        self.derivative_funcs = derivative_funcs
        self.before_x_vector = []
        self.iterations = 0
        self.x_left, self.x_right = None, None
        self.y_left, self.y_right = None, None

    def calculate(self, x, y):
        """
        Вычисляет значения функций системы уравнений в заданных точках.

        Args:
            x (float): Координата x.
            y (float): Координата y.

        Returns:
            numpy.ndarray: Массив значений функций.
        """
        return np.array([self.funcs[0](x, y), self.funcs[1](x, y)])

    def calculate_derivatives(self, *args):
        """
        Вычисляет значения производных функций системы уравнений в заданных точках.

        Args:
            *args: Аргументы точки, в которой вычисляются производные.

        Returns:
            numpy.ndarray: Массив значений производных функций.
        """
        return np.array([f(*args) for f in self.derivative_funcs])

    def get_error_rate(self):
        """
        Вычисляет ошибку приближения решения системы.

        Returns:
            numpy.ndarray: Массив значений ошибок приближения.
        """
        return abs(np.array(self.before_x_vector) - self.solutions)

    def _get_sufficient_convergence_condition(self, x, y):
        """
        Вычисляет значение достаточного условия сходимости итерационного процесса.

        Args:
            x (float): Координата x.
            y (float): Координата y.

        Returns:
            float: Значение достаточного условия сходимости.
        """
        return max(sum(abs(i)) for i in self.calculate_derivatives(x, y))

    def check_sufficient_convergence_condition(self, x, y):
        """
        Проверяет выполнение достаточного условия сходимости итерационного процесса.

        Args:
            x (float): Координата x.
            y (float): Координата y.

        Returns:
            bool: True, если достаточное условие сходимости выполняется, False в противном случае.
        """
        return self._get_sufficient_convergence_condition(x, y) < 1

    def solve(self):
        """
        Решает систему уравнений методом простых итераций.

        Returns:
            numpy.ndarray: Массив решений системы уравнений.
        """
        return self.simple_iteration_method()

    def _enter_root_isolation(self):
        """
        Вводит интервал изоляции корня системы уравнений.
        """
        print("Введите интервал изоляции корня:")
        x_left = InputCorrect.get_float_input("\tЛевый конец отрезка по x: ")
        x_right = InputCorrect.get_float_input("\tПравый конец отрезка по x: ")
        y_left = InputCorrect.get_float_input("\tЛевый конец отрезка по y: ")
        y_right = InputCorrect.get_float_input("\tПравый конец отрезка по y: ")
        while not (self.calculate(x_left, y_left)[0] * self.calculate(x_right, y_right)[0] < 0 and
                   self.calculate(x_left, y_left)[1] * self.calculate(x_right, y_right)[1] < 0):
            if not (x_left < x_right and y_left < y_right):
                print("Значения левых концов должны быть меньше правых.")
                self._enter_root_isolation(self)
            print("Значения функции на углах квадрата должны быть разного знака для обеих функций!")
            if InputCorrect.get_yes_or_no_input(f"Показать график системы для корректировки?"):
                self.draw_graphic(x_left, x_right, y_left, y_right)
            print("Введите другие значения концов:")
            x_left = InputCorrect.get_float_input("\tЛевый конец отрезка по x: ")
            x_right = InputCorrect.get_float_input("\tПравый конец отрезка по x: ")
            y_left = InputCorrect.get_float_input("\tЛевый конец отрезка по y: ")
            y_right = InputCorrect.get_float_input("\tПравый конец отрезка по y: ")
        self.x_left, self.x_right = min(x_left, x_right), max(x_left, x_right)
        self.y_left, self.y_right = min(y_left, y_right), max(y_left, y_right)

    def draw_graphic(self, x_left=None, x_right=None, y_left=None, y_right=None):
        """
        Рисует график системы уравнений на заданном интервале.

        Args:
            x_left (float, optional): Левый конец отрезка по x. Defaults to None.
            x_right (float, optional): Правый конец отрезка по x. Defaults to None.
            y_left (float, optional): Левый конец отрезка по y. Defaults to None.
            y_right (float, optional): Правый конец отрезка по y. Defaults to None.
        """
        if None in [x_left, x_right, y_left, y_right]:
            if None in [self.x_left, self.x_right, self.y_left, self.y_right]:
                print("Невозможно нарисовать график. Не определены концы отрезка")
                return
            else:
                x_left = self.x_left
                x_right = self.x_right
                y_left = self.y_left
                y_right = self.y_right
        x = np.arange(x_left, x_right, abs(x_left - x_right) / 30)
        y = np.arange(y_left, x_right, abs(y_left - y_right) / 30)
        x, y = np.meshgrid(x, y)
        z = self.calculate(x, y)
        fig = plt.figure()
        ax = fig.add_subplot(projection='3d')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.plot_surface(x, y, z[0], cmap=cm.coolwarm)
        ax.plot_surface(x, y, z[1], cmap="plasma")
        plt.show()

    def simple_iteration_method(self):
        """
        Решает систему уравнений методом простых итераций.

        Returns:
            numpy.ndarray: Массив решений системы уравнений.
        """
        self._enter_root_isolation()
        if InputCorrect.get_yes_or_no_input("Показать график системы?"):
            self.draw_graphic()

        x = InputCorrect.get_float_input("Введите начальное приближение по x: ")
        y = InputCorrect.get_float_input("Введите начальное приближение по y: ")
        while not (self.x_left < x < self.x_right and self.y_left < y < self.y_right):
            print("Начальное приближение должно быть внутри интервала изоляции корня!")
            x = InputCorrect.get_float_input("Введите начальное приближение по x: ")
            y = InputCorrect.get_float_input("Введите начальное приближение по y: ")

        if not self.check_sufficient_convergence_condition(x, y):
            print("Не выполняется достаточное условие сходимости итерационного процесса.")
            print("Попробуйте ввести другое начальное приближение.")
            if not InputCorrect.get_yes_or_no_input("Продолжить выполнение?"):
                return

        lambda_x = -1
        phi_x = lambda x, y: x + self.calculate(x, y)[0] / lambda_x
        lambda_y = -1
        phi_y = lambda x, y: y + self.calculate(x, y)[1] / lambda_y
        epsilon = 10 ** (-5)
        self.before_x_vector = [x + 100, y + 100]
        while max(abs(x - self.before_x_vector[0]),
                  abs(y - self.before_x_vector[1])) > epsilon and self.iterations <= 100000:
            self.before_x_vector[0], self.before_x_vector[1] = x, y
            x, y = phi_x(x, y), phi_y(x, y)
            self.iterations += 1
        self.solutions = np.array([x, y])
        return self.solutions
