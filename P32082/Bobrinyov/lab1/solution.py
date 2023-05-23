def input_from_file(path):
    try:
        n = 0
        nq = 0
        a = []
        with open(path, 'r', encoding='utf-8') as file:
            n = int(file.readline().strip())
            for line in file:
                if (line != '\n') and (line != ' ') and (line != ' \n'):
                    nq += 1
        if nq != n:
            print('Указано неверное количество уравнений')
            return
        file.close()
        with open(path, 'r', encoding='utf-8') as file:
            next(file)
            for row in file:
                line = list(row.split())
                if (line[-2] != '|') or (len(line) - 2 != n):
                    print('Файл имеет ошибку формата! Исправьте и попробуйте снова.')
                    return
                a.append(list(line))
        file.close()
        calculator = Calculator(n, optimize(a, n))
        calculator.calculate()
        del calculator
    except FileNotFoundError:
        print('Файл не был найден!')
    except ValueError:
        print('Некорректные данные в файле')


def input_from_console():
    try:
        n = int(input('Укажите размерность матрицы (не более 20): '))
        if (n <= 20) or (n > 1):
            a = []
            print('Введите коэффициенты уравнения в формате:')
            print('ai1 ai2 ... aij | bi')
            for i in range(n):
                while True:
                    line = list((input(str(i + 1) + ': ').split()))
                    if (int(len(line)) - 2 != n) or (line[-2] != '|'):
                        print('Кол-во строк не равно кол-ву столбцов или неправильный формат')
                        print('Попробуйте снова:')
                    else:
                        a.append(line)
                        break
            calculator = Calculator(n, optimize(a, n))
            calculator.calculate()
            del calculator
        else:
            print('Неправильный ввод!')
            return
    except ValueError:
        print('Неправильный ввод!')


#Гарантирует, что все элементы матрицы будут числами с плавающей запятой
def optimize(arr, n):
    i = 0
    while i < n:
        j = 0
        while j < n:
            arr[i][j] = float(arr[i][j])
            j += 1
        arr[i][j + 1] = float(arr[i][j + 1])
        i += 1
    return arr


class Calculator:
    n = 0           #Количество уравнений и неизвестных
    x = []          #Вектор неизвестных
    system = []     #Система уравнений
    det = 0         #Определитель
    swap = 0        #Кол-во перестановок

    def __init__(self, n, system):
        self.n = n
        self.system = system
        self.x = []
        self.swap = 0

    def calculate(self):
        try:
            print('\nНаша система:')
            self.__print_system()

            self.__make_triangle()
            print('\nТреугольная матрица:')
            self.__print_system()

            self.__get_determinate()

            self.__calc_vector_x()
            self.__print_vector_x()

            self.__print_vector_residuals()
        except ZeroDivisionError:
            return
        except ArithmeticError:
            return

    #Если в процессе вычисления a11, a22, a33, ... = 0 - нужно переставить соответственно коэф.
    def __check_diagonal(self, i):
        j = i
        while j < self.n:
            if (self.system[j][i] != 0) and (self.system[i][j] != 0):
                swap = self.system[j]
                self.system[j] = self.system[i]
                self.system[i] = swap
                self.swap += 1
                return
            j += 1
        print('Нет решений!')
        return ArithmeticError

    #Вычисление треугольной матрицы
    def __make_triangle(self):
        try:
            i = 0
            while i < self.n:
                if self.system[i][i] == 0:
                    self.__check_diagonal(i)
                m = i
                while m < self.n - 1:
                    a = -(self.system[m + 1][i] / self.system[i][i])
                    j = i
                    while j < self.n:
                        self.system[m + 1][j] += a * self.system[i][j]
                        j += 1
                    self.system[m + 1][-1] += a * self.system[i][-1]
                    m += 1
                k = 0
                line_sum = 0
                while k < self.n:
                    line_sum += self.system[i][k]
                    k += 1
                if line_sum == 0:
                    print('Данная система не совместима, решений нет!')
                    return ArithmeticError
                i += 1
        except ValueError:
            print('Некорректная работа с данными!')
            return

    #Вывод системы на экран
    def __print_system(self):
        i = 0
        while i < self.n:
            j = 0
            while j < self.n:
                print(self.system[i][j], 'x[' + str(j) + '] ', end='')
                j += 1
            print(self.system[i][-2], self.system[i][-1])
            i += 1

    #Подсчет и вывод определителя на экран
    def __get_determinate(self):
        i = 0
        self.det = 1
        while i < self.n:
            self.det *= self.system[i][i]
            i += 1
        if self.swap % 2 == 1:
            self.det *= -1
        print(f'\nОпределитель = {self.det}\n')
        if self.det == 0:
            print('Система является вырожденной, нет решения.')
            return ArithmeticError

    #Подсчет неизвестных x1, x2, x3, ..., xn
    def __calc_vector_x(self):
        i = self.n - 2
        self.x.append(self.system[self.n - 1][-1] / self.system[self.n - 1][self.n - 1])
        while i > -1:
            k = self.n - 1
            val = self.system[i][-1]
            while k > i:
                val -= self.x[self.n - 1 - k] * self.system[i][k]
                k -= 1
            self.x.append(val / self.system[i][i])
            i -= 1

    def __print_vector_x(self):
        i = 0
        print('Решение системы:')
        self.x.reverse()
        while i < self.n:
            print('x[' + str(i) + ']:', self.x[i])
            i += 1
        print('')

    #Подсчет коэф. невязки r1, r2, r3, ..., rn и вывод на экран
    def __print_vector_residuals(self):
        i = 0
        print('Невязки:')
        while i < self.n:
            res = 0
            j = 0
            while j < self.n:
                res += self.system[i][j] * self.x[j]
                j += 1
            res -= self.system[i][-1]
            i += 1
            print('Невязка для', i, 'строки:', abs(res))
        print('')
