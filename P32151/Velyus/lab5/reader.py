from sympy import lambdify, sympify, symbols
from sympy.abc import x
from sympy import Symbol

class Reader:
    __FILE = "0"
    __CONSOLE = "1"

    __filepath = "file.txt"
    __file = None
    __read_type = __CONSOLE

    def __init__(self):
        """
            Класс, предназначенный для чтения ввода от пользователя или из файла.

            Атрибуты:
                __FILE (str): Константа для обозначения типа ввода - файл.
                __CONSOLE (str): Константа для обозначения типа ввода - консоль.
                __filepath (str): Путь к файлу для чтения ввода.
                __file (file): Файловый объект для чтения ввода из файла.
                __read_type (str): Текущий тип ввода.

            Методы:
                __read_function(): Вспомогательный метод для чтения строки ввода в зависимости от типа ввода.
                __file_init(): Вспомогательный метод для инициализации файла для чтения ввода.
                close_file(): Закрывает файловый объект после чтения ввода из файла.
                read_answer(options, error_message, handler): Считывает ответ пользователя с проверкой и обработкой ошибок.
                print_question(question): Выводит вопрос пользователю для консольного ввода.
                is_contains_options(option, options): Проверяет, содержится ли вариант ответа в списке допустимых вариантов.
                is_float(option, options): Проверяет, является ли значение числом с плавающей точкой.
                is_int(option, options): Проверяет, является ли значение целым числом.
                is_in_range(option, options): Проверяет, находится ли значение в указанном диапазоне.
                is_string(option, options): Всегда возвращает True, используется для обработки вопросов без проверки.
                is_float_list(option, options): Проверяет, является ли строка списком чисел с плавающей точкой.
                is_eq(option, options): Проверяет, является ли введенное выражение корректным выражением с одной переменной 'x'.
        """
        self.print_question("Выберите тип ввода\n(1) Файл\n(2) Консоль")
        option = self.read_answer(["1", "2"], "Введите 1 или 2", self.is_contains_options)
        self.__read_type = self.__FILE if option == "1" else self.__CONSOLE

        if self.__read_type == self.__FILE:
            self.__file_init()

    def __read_function(self):
        """
            Вспомогательный метод для чтения строки ввода в зависимости от типа ввода.
        """
        if self.__read_type == self.__CONSOLE:
            return input()

        return self.__file.readline()

    def __file_init(self):
        """
            Вспомогательный метод для инициализации файла для чтения ввода.
        """
        try:
            self.__file = open(self.__filepath, mode="r")
        except IOError:
            print(f"Не удается получить доступ к файлу {self.__filepath}")
            exit()

    def close_file(self):
        """
            Закрывает файловый объект после чтения ввода из файла.
        """
        self.__file.close()

    def read_answer(self, options, error_message, handler):
        """
            Считывает ответ пользователя с проверкой и обработкой ошибок.

            Параметры:
                options (list): Список допустимых вариантов ответа.
                error_message (str): Сообщение об ошибке при некорректном вводе.
                handler (function): Функция-обработчик для проверки корректности ответа.

            Возвращает:
                str: Введенный ответ пользователя.
        """
        while True:
            option = self.__read_function().strip()
            if handler(option, options):
                break
            self.print_question(error_message)
        return option

    def print_question(self, question):
        """
            Выводит вопрос пользователю для консольного ввода.
        """
        if self.__read_type == self.__CONSOLE:
            print(question)

    @staticmethod
    def is_contains_options(option, options):
        """
            Проверяет, содержится ли вариант ответа в списке допустимых вариантов.
        """
        return option in options

    @staticmethod
    def is_float(option, options):
        """
            Проверяет, является ли значение числом с плавающей точкой.
        """
        try:
            float(option)
            return True
        except ValueError:
            return False

    @staticmethod
    def is_int(option, options):
        """
            Проверяет, является ли значение целым числом.
        """
        try:
            int(option)
            return True
        except ValueError:
            return False

    @staticmethod
    def is_in_range(option, options):
        """
            Проверяет, находится ли значение в указанном диапазоне.
        """
        try:
            return options[0] <= options[2](option) <= options[1]
        except ValueError:
            return False

    @staticmethod
    def is_string(option, options):
        return True

    @staticmethod
    def is_float_list(option, options):
        try:
            list(map(float, option.split()))
            return True
        except ValueError:
            return False

    @staticmethod
    def is_eq(option, options):
        try:
            eq = sympify(option)
            return len(eq.atoms(Symbol)) == 1 and Symbol("x") in eq.atoms(Symbol)
        except (SyntaxError, ValueError):
            return False
