from solution import input_from_file as iff, input_from_console as ifc

print('\n*Решение СЛАУ методом Гаусса*')

while True:
    try:
        print('\nДоступные функции:')
        print('1: Считывание системы из файла')
        print('2: Ввод системы с клавиатуры')
        print('3: Выход')
        param = int(input('Выберите действие (1-3): '))

        if param == 1:
            print('Выбран способ считывание с файла.')
            print('Файл должен содержать линейную систему вида (размерность не более n = 20):\n\n')
            print('a11 a12 ... a1n | b1\n')
            print('a21 a22 ... a2n | b2\n')
            print('... ... ... ... | ..\n')
            print('an1 an2 ... ann | bn\n')
            
            iff(input('Путь к файлу: ').strip())
        elif param == 2:
            print('Выбран способ ввода вручную')
            ifc()
        elif param == 3:
            print('Выход!')
            break
        else:
            print('Неправильно введено значение! Попробуйте снова')
    except KeyboardInterrupt:
        print('Прервано')
    except:
        print('Что-то пошло не так')