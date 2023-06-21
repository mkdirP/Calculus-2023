class InputCorrect:
    """Класс для управления вводом данных"""

    @staticmethod
    def string_input(message=""):
        """
        Запрашивает ввод строки от пользователя.
        Args:
            message (str, optional): Сообщение, отображаемое перед вводом. Defaults to "".
        Returns:
            str: Введенная пользователем строка.
        """
        buffer = ""
        while buffer == "":
            buffer = input(message).strip()
        return buffer

    @staticmethod
    def _convert_to_number(num):
        """Преобразует строку в число."""
        try:
            return float(num.replace(',', '.'))
        except ValueError:
            return None

    @staticmethod
    def get_float_input(message=""):
        """
        Запрашивает ввод числа с плавающей точкой от пользователя.
        Args:
            message (str, optional): Сообщение, отображаемое перед вводом. Defaults to "".
        Returns:
            float: Введенное пользователем число.
        """
        number = None
        while number is None:
            try:
                number = InputCorrect._convert_to_number(InputCorrect.string_input(message))
            except ValueError:
                print("Ошибка: Введите корректное число.")
        return number

    @staticmethod
    def get_yes_or_no_input(message=""):
        """
        Запрашивает ввод ответа "да" или "нет" от пользователя.
        Args:
            message (str, optional): Сообщение, отображаемое перед вводом. Defaults to "".
        Returns:
            bool: True, если пользователь ввел "да", False в противном случае.
        """
        answer = ""
        while answer.lower() not in ["y", "n", "д", "н"]:
            answer = InputCorrect.string_input(message + " [y/n]: ")
        return answer.lower() in ["y", "д"]

    @staticmethod
    def get_enum_input(variants_list, message):
        """
        Запрашивает выбор значения из списка вариантов.
        Args:
            variants_list (list): Список доступных вариантов.
            message (str): Сообщение, отображаемое перед вводом.
        Returns:
            str: Выбранный вариант.
        """
        buffer = ""
        while buffer not in variants_list:
            buffer = InputCorrect.string_input(message)
        return buffer

    @staticmethod
    def print_variants(variant_list, values_list):
        """
        Выводит список вариантов с соответствующими значениями.
        Args:
            variant_list (list): Список вариантов.
            values_list (list): Список соответствующих значений.
        """
        for i, variant in enumerate(variant_list):
            print(f"{i + 1}. {variant}")

    @staticmethod
    def get_choice_index(n):
        """
        Запрашивает у пользователя индекс выбранного варианта.
        Args:
            n (int): Количество доступных вариантов.
        Returns:
            int: Индекс выбранного варианта.
        """
        choice = None
        while choice is None:
            try:
                choice = int(InputCorrect.string_input(f"Введите число от 1 до {n}: "))
                if not 1 <= choice <= n:
                    raise ValueError
            except ValueError:
                print("Ошибка: Введите корректное число.")
        return choice

    @staticmethod
    def get_multiple_choice_input(variant_list, values_list, message=""):
        """
        Запрашивает выбор из списка вариантов с соответствующими значениями.
        Args:
            variant_list (list): Список вариантов.
            values_list (list): Список соответствующих значений.
            message (str, optional): Сообщение, отображаемое перед вводом. Defaults to "".
        Raises:
            ValueError: Если списки вариантов и значений не совпадают по длине.
        Returns:
            any: Выбранное значение.
        """
        n = len(variant_list)
        if n == 0 or len(variant_list) != len(values_list):
            raise ValueError

        if message:
            print(message)

        InputCorrect.print_variants(variant_list, values_list)

        choice_index = InputCorrect.get_choice_index(n) - 1
        return values_list[choice_index]

