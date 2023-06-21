class IntegralMethod:
    """
    Класс, содержащий статические методы для численного интегрирования различными методами.
    """
    @staticmethod
    def left_rectangle(integral, left_cut, right_cut, n):
        """
        Метод прямоугольников (левая сумма).
        :param integral: Объект Integral, представляющий интеграл.
        :param left_cut: Левый предел интегрирования.
        :param right_cut: Правый предел интегрирования.
        :param n: Количество шагов разбиения.
        :return: Приближенное значение интеграла методом прямоугольников (левая сумма).
        """
        result = 0
        step = abs(left_cut - right_cut) / n
        i = left_cut
        while i < right_cut:
            result += integral.calculate(i)
            i += step
        return result * step

    @staticmethod
    def center_rectangle(integral, left_cut, right_cut, n):
        """
        Метод прямоугольников (средняя сумма).
        :param integral: Объект Integral, представляющий интеграл.
        :param left_cut: Левый предел интегрирования.
        :param right_cut: Правый предел интегрирования.
        :param n: Количество шагов разбиения.
        :return: Приближенное значение интеграла методом прямоугольников (средняя сумма).
        """
        result = 0
        step = abs(left_cut - right_cut) / n
        i = left_cut + step / 2
        while i < right_cut:
            result += integral.calculate(i)
            i += step
        return result * step

    @staticmethod
    def right_rectangle(integral, left_cut, right_cut, n):
        """
        Метод прямоугольников (правая сумма).
        :param integral: Объект Integral, представляющий интеграл.
        :param left_cut: Левый предел интегрирования.
        :param right_cut: Правый предел интегрирования.
        :param n: Количество шагов разбиения.
        :return: Приближенное значение интеграла методом прямоугольников (правая сумма).
        """
        result = 0
        step = abs(left_cut - right_cut) / n
        i = left_cut + step
        while i <= right_cut:
            result += integral.calculate(i)
            i += step
        return result * step

    @staticmethod
    def trapezoid_method(integral, left_cut, right_cut, n):
        """
        Метод трапеций.
        :param integral: Объект Integral, представляющий интеграл.
        :param left_cut: Левый предел интегрирования.
        :param right_cut: Правый предел интегрирования.
        :param n: Количество шагов разбиения.
        :return: Приближенное значение интеграла методом трапеций.
        """
        result = 0
        step = abs(left_cut - right_cut) / n
        i = left_cut + step
        while i < right_cut:
            result += integral.calculate(i)
            i += step
        result += (integral.calculate(left_cut) + integral.calculate(right_cut)) / 2
        return result * step

    @staticmethod
    def simpson_method(integral, left_cut, right_cut, n):
        """
        Метод Симпсона.
        :param integral: Объект Integral, представляющий интеграл.
        :param left_cut: Левый предел интегрирования.
        :param right_cut: Правый предел интегрирования.
        :param n: Количество шагов разбиения (должно быть четным).
        :return: Приближенное значение интеграла методом Симпсона.
        """
        result = 0
        step = abs(left_cut - right_cut) / n
        for i in range(1, n):
            if i % 2:
                result += 2 * integral.calculate(left_cut + step * i)
            else:
                result += 4 * integral.calculate(left_cut + step * i)
        result += integral.calculate(left_cut) + integral.calculate(right_cut)
        return result * step / 3
