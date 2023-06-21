import numpy as np
from matplotlib import pyplot as plt

from InputCorrect import InputCorrect


class Integral:
    """
    Класс, представляющий интеграл заданной функции.
    """

    def __init__(self, func):
        """
        Инициализация объекта интеграла.
        :param func: Функция, подлежащая интегрированию.
        """
        self.func = func
        self.steps = 0
        self.left = None
        self.right = None
        self.iterations = 0

    def calculate(self, x):
        """
        Вычисляет значение функции для заданного аргумента.
        :param x: Значение аргумента.
        :return: Значение функции для заданного аргумента.
        """
        return self.func(x)

    def set_steps(self, steps):
        """
        Устанавливает количество шагов интегрирования.
        :param steps: Количество шагов.
        """
        self.steps = steps

    def solve(self, left_cut, right_cut, method_func):
        """
        Выполняет численное интегрирование функции на заданном интервале с использованием указанного метода.
        :param left_cut: Левый предел интегрирования.
        :param right_cut: Правый предел интегрирования.
        :param method_func: Функция, реализующая выбранный метод интегрирования.
        :return: Результат интегрирования или None, если интеграл не существует или не удалось вычислить.
        """
        self.left = left_cut
        self.right = right_cut
        try:
            steps = 4
            epsilon = InputCorrect.get_epsilon_input("Введите эпсилон: ")
            while abs(method_func(self, left_cut, right_cut, steps / 2) - method_func(self, left_cut, right_cut, steps)) > epsilon \
                    and self.iterations < 19:
                steps *= 2
                self.iterations += 1
            self.set_steps(steps)
            return round(method_func(self, left_cut, right_cut, steps), len(str(int(1 / epsilon))))
        except Exception:
            return None

    def draw_function(self, left_cut=None, right_cut=None):
        """
        Рисует график функции на указанном интервале.
        Если интервал не указан, используются пределы, заданные при вызове solve().
        :param left_cut: Левый предел интервала.
        :param right_cut: Правый предел интервала.
        """
        if left_cut is None or right_cut is None:
            if self.left is None or self.right is None:
                print("Невозможно нарисовать график. Не определены концы отрезка")
            else:
                left_cut = self.left
                right_cut = self.right
        x_axis = np.linspace(min(left_cut, right_cut), max(left_cut, right_cut), 100)
        plt.plot(x_axis, self.calculate(x_axis))
        plt.grid(True, which='both')
        plt.axvline(x=0, color='k')
        plt.axhline(y=0, color='k')
        plt.show()
