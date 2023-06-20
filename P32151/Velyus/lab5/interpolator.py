import matplotlib.pyplot as plt
import sympy


class Interpolator:
    @staticmethod
    def finite_differences(x_list, y_list):
        """
            Вычисляет конечные разности для списка точек.

            Параметры:
                x_list (list): Список значений x.
                y_list (list): Список значений y.

            Возвращает:
                list: Список конечных разностей.
        """
        n = len(x_list)
        plug = "-"
        differences = [[plug] * (n + 1) for _ in range(n)]

        for y in range(n + 1):
            for x in range(n):
                if y == 0:
                    differences[x][y] = x_list[x]
                elif y == 1:
                    differences[x][y] = y_list[x]
                elif x != n - 1 and differences[x + 1][y - 1] != plug:
                    differences[x][y] = differences[x + 1][y - 1] - differences[x][y - 1]

        return differences

    @staticmethod
    def lagrange_method(x_list, y_list, x0):
        """
            Выполняет интерполяцию методом Лагранжа для заданного x0.

            Параметры:
                x_list (list): Список значений x.
                y_list (list): Список значений y.
                x0 (float): Значение x, для которого выполняется интерполяция.

            Возвращает:
                float: Результат интерполяции методом Лагранжа.
        """
        result = 0
        for y_index in range(len(y_list)):
            mul = 1
            for x_index in range(len(x_list)):
                mul *= (x0 - x_list[x_index]) / (x_list[y_index] - x_list[x_index]) if x_index != y_index else 1
            result += y_list[y_index] * mul
        return result

    @staticmethod
    def gauss_method(x_list, differences, x0):
        """
            Выполняет интерполяцию методом Гаусса для заданного x0.

            Параметры:
                x_list (list): Список значений x.
                differences (list): Список конечных разностей.
                x0 (float): Значение x, для которого выполняется интерполяция.

            Возвращает:
                float: Результат интерполяции методом Гаусса.
        """
        differences = [row[1:] for row in differences]
        middle = len(x_list) // 2 + len(x_list) % 2 - 1
        x = x_list[middle]

        y_values = []
        k = 0 if x >= x0 else 1
        row = middle

        for ind in range(len(differences)):
            if differences[row][ind] == "-":
                break

            y_values.append(differences[row][ind])

            if ind % 2 == k:
                row -= 1

        t = (x0 - x) / (x_list[1] - x_list[0])
        num = 1
        coefficients = [1, t]

        for ind in range(2, len(y_values)):
            if (k == 0 and ind % 2 == 0) or (k == 1 and ind % 2 != 0):
                coefficients.append(coefficients[-1] * (t + num) / ind)
            else:
                coefficients.append(coefficients[-1] * (t - num) / ind)

            if ind % 2 != 0:
                num += 1

        result = sum(y_values[ind] * coefficients[ind] for ind in range(len(y_values)))
        return result

    @staticmethod
    def show_graph(x_list, y_list, differences, x0, results, eq=None):
        """
        Отображает график исходных данных, интерполяционных многочленов и исходной функции (при наличии).

        Параметры:
            x_list (list): Список значений x.
            y_list (list): Список значений y.
            differences (list): Список конечных разностей.
            x0 (float): Значение x, для которого выполняется интерполяция.
            results (list): Список результатов интерполяции для отображения на графике.
            eq (sympy.Expr, optional): Исходная функция. По умолчанию None.
        """
        plt.figure()
        plt.grid(True)

        left = min(x_list)
        right = max(x_list)
        dot_count = 1000
        step = (right - left) / (dot_count - 1)
        x_dots = []

        for n in range(dot_count):
            x = left + step * n
            x_dots.append(x)

        y_dots_lagrange = [Interpolator.lagrange_method(x_list, y_list, dot) for dot in x_dots]
        y_dots_gauss = [Interpolator.gauss_method(x_list, differences, dot) for dot in x_dots]

        x_dots_eq = []
        y_dots_eq = []
        if eq:
            for n in range(dot_count):
                try:
                    x = left + step * n
                    y = eq(x)

                    if x == sympy.core.numbers.NegativeInfinity or x == sympy.core.numbers.Infinity or str(x) == "nan":
                        continue
                    if y == sympy.core.numbers.NegativeInfinity or y == sympy.core.numbers.Infinity or str(y) == "nan":
                        continue

                    x_dots_eq.append(x)
                    y_dots_eq.append(y)
                except TypeError:
                    continue

        plt.plot(x_dots, y_dots_lagrange, label="Многочлен Лагранжа", color="#e59500")
        plt.plot(x_dots, y_dots_gauss, label="Многочлен Гаусса", color="#840032")
        if eq:
            plt.plot(x_dots_eq, y_dots_eq, label="Исходная функция", color="#6B00C7")
        plt.scatter(x_list, y_list, label="Исходные данные", color="#002642")
        plt.scatter(x0, results[0], label="x0", color="#e59500")
        plt.scatter(x0, results[1], label="x0", color="#840032")

        plt.legend(fontsize="x-small")
        plt.show()