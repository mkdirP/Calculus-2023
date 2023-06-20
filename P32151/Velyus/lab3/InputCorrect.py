class InputCorrect:
    """
    Класс, предоставляющий методы для корректной обработки пользовательского ввода.
    """

    @staticmethod
    def string_input(message=""):
        """
        Запрашивает у пользователя ввод строки и возвращает ее.
        :param message: Сообщение, выводимое перед запросом ввода.
        :return: Введенная пользователем строка.
        """
        buf = ""
        while buf == "":
            buf = input(message).strip()
        return buf

    @staticmethod
    def _convert_to_number(num):
        """
        Преобразует строку в число.
        :param num: Строка, представляющая число.
        :return: Преобразованное число или None, если преобразование не удалось.
        """
        try:
            return float(num.replace(',', '.'))
        except ValueError:
            return None

    @staticmethod
    def get_float_input(message=""):
        """
        Запрашивает у пользователя ввод числа и возвращает его в виде числового значения.
        :param message: Сообщение, выводимое перед запросом ввода.
        :return: Введенное пользователем число.
        """
        number = None
        while number is None:
            number = InputCorrect._convert_to_number(InputCorrect.string_input(message))
        return number

    @staticmethod
    def get_yes_or_no_input(message=""):
        """
        Запрашивает у пользователя ответ "да" или "нет" и возвращает соответствующее булево значение.
        :param message: Сообщение, выводимое перед запросом ввода.
        :return: True, если пользователь ответил "да", False в противном случае.
        """
        answer = "0"
        while answer[0].lower() not in ["y", "n", "д", "н"]:
            answer = InputCorrect.string_input(message + " [y/n]: ")
        return answer[0].lower() in ["y", "д"]

    @staticmethod
    def get_enum_input(variants_list, message):
        """
        Запрашивает у пользователя выбор из списка вариантов и возвращает выбранный вариант.
        :param variants_list: Список доступных вариантов.
        :param message: Сообщение, выводимое перед запросом ввода.
        :return: Выбранный вариант.
        """
        buf = ""
        while buf not in variants_list:
            buf = InputCorrect.string_input(message)
        return buf

    @staticmethod
    def get_multiple_choice_input(variant_list, values_list, message=""):
        """
        Запрашивает у пользователя выбор из списка вариантов и возвращает соответствующее значение.
        :param variant_list: Список вариантов.
        :param values_list: Список соответствующих значений.
        :param message: Сообщение, выводимое перед запросом ввода.
        :return: Значение, соответствующее выбранному варианту.
        :raises ValueError: Если списки вариантов и значений имеют разную длину или если список вариантов пуст.
        """
        n = len(variant_list)
        if n == 0 or len(variant_list) != len(values_list):
            raise ValueError

        if message != "":
            print(message)

        for i in range(n):
            s = f"{i + 1}."
            lines = variant_list[i].split('\n')
            print('\t' + s, lines[0])
            for line in lines[1:]:
                print("\t" + ' ' * len(s), line)

        i = int(InputCorrect.get_enum_input([str(i) for i in range(1, n + 1)], f"Введите число от 1 до {n}: ")) - 1
        return values_list[i]

    @staticmethod
    def get_epsilon_input(message=""):
        """
        Запрашивает у пользователя ввод значения эпсилон и возвращает его.
        :param message: Сообщение, выводимое перед запросом ввода.
        :return: Введенное пользователем значение эпсилон.
        """
        e = InputCorrect.get_float_input(message)
        while not (0 < e <= 1):
            print("Эпсилон должно быть в промежутке от 0 до 1!")
            e = InputCorrect.get_float_input(message)
        return e
