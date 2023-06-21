import functions
import methods

n = 4
a, b = [float(x) for x in input("Выберите интервал(<a> <b>):").replace(",", ".").split()]
inp_func = input("Выберите уравнение(f1 - уравнение 1, f2 - уравнение 2, f3 - уравнение 3):\n")

if inp_func == 'f1':
    func = functions.func1
elif inp_func == 'f2':
    func = functions.func2
elif inp_func == 'f3':
    func = functions.func3
else:
    print("Wrong func input")
    exit()

eps = float(input("Введите эпсилон:\n").replace(",", "."))
inp_method = input(
    "Выберите метод(rl - левые прямоугольники, rm - средние, rr - правые, tr - трапеция, sm - Симпсон):\n")

if inp_method[0] == 'r':
    type = ''
    if inp_method == 'rl':
        type = 'left'
    elif inp_method == 'rm':
        type = 'middle'
    elif inp_method == 'rr':
        type = 'right'
    i_0 = methods.methodOfRectangle(type, func, a, b, n)
    i_1 = methods.methodOfRectangle(type, func, a, b, 2 * n)
    while abs(i_0 - i_1) > eps:
        n = 2 * n
        i_0 = methods.methodOfRectangle(type, func, a, b, n)
        i_1 = methods.methodOfRectangle(type, func, a, b, 2 * n)
    print("Answer: " + str(i_1))
elif inp_method == 'tr':
    i_0 = methods.methodOfTrapeze(func, a, b, n)
    i_1 = methods.methodOfTrapeze(func, a, b, 2 * n)
    while abs(i_0 - i_1) > eps:
        n = 2 * n
        i_0 = methods.methodOfTrapeze(func, a, b, n)
        i_1 = methods.methodOfTrapeze(func, a, b, 2 * n)
    print("Answer: " + str(i_1))
elif inp_method == 'sm':
    i_0 = methods.methodOfSimpson(func, a, b, n)
    i_1 = methods.methodOfSimpson(func, a, b, 2 * n)
    while abs(i_0 - i_1) > eps:
        n = 2 * n
        i_0 = methods.methodOfSimpson(func, a, b, n)
        i_1 = methods.methodOfSimpson(func, a, b, 2 * n)
    print("Answer: " + str(i_1))
else:
    print("Wrong method input")
    exit()

# print(methods.methodOfRectangle('right', functions.func1, 1, 2, 5))
# print(methods.methodOfTrapeze(functions.func1, 1, 2, 10))
# print(methods.methodOfSimpson(functions.func1, 1, 2, 4))
