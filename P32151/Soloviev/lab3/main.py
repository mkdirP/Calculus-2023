import math


def choose_func_type():
    while True:
        try:
            print("Choose function type")
            for i in [1, 2]:
                print(str(i) + ")", get_func_type_name(i))
            chosen_type = int(input(">>>"))
            if chosen_type in [1, 2]:
                print("Chosen function:", get_func_type_name(chosen_type))
                return chosen_type
        except:
            print("\033[31m{}".format("Error: Invalid input. Choose int number between 1 and 2."))
            print("\033[0m".format(), end='')
            pass


def get_func_type_name(num):
    if num == 1:
        return "Function with no break"
    if num == 2:
        return "Function with break"


def simple_integral_calculation(func, chosen_method, a, b, e, k):
    n = 4
    integral = -10
    integral_prev = e * 2
    while abs((integral_prev - integral) / (2 ** k - 1)) > e:
        integral_prev = integral
        integral = 0
        h = (abs(a - b)) / n
        for i in range(n):
            integral += get_method(chosen_method, func, a + h * i, a + h * (i + 1))
        n *= 2

    return integral, n / 2, abs((integral_prev - integral) / (2 ** k - 1))


def first_break_integral_calculation(func, method_func, a, b, br, e):
    if a <= br <= b:
        if a == br:
            return second_break_integral_calculation(func, method_func, a + e, b, e, 4)[0]
        elif b == br:
            return second_break_integral_calculation(func, method_func, a, b - e, e, 4)[0]
        else:
            return second_break_integral_calculation(func, method_func, a, br - e, e, 4)[0] + \
                   second_break_integral_calculation(func, method_func, br + e, b, e, 4)[0]
    else:
        return second_break_integral_calculation(func, method_func, a, b, e, 4)[0]


def second_break_integral_calculation(func, method_func, a, b, br, err):
    if a <= br <= b:
        if a == br:
            return simple_integral_calculation(func, method_func, a + err, b, err, 4)[0]
        if b == br:
            return simple_integral_calculation(func, method_func, a, b - err, err, 4)[0]

        return simple_integral_calculation(func, method_func, a, br - err, err, 4)[0] + \
               simple_integral_calculation(func, method_func, br + err, b, err, 4)[0]
    else:
        return simple_integral_calculation(func, method_func, a, b, err, 4)[0]


def choose_func():
    while True:
        try:
            print("Choose a function to integrate:")
            for i in [1, 2, 3]:
                print(str(i) + ")", get_func_name(i))
            chosen_func = int(input(">>>"))
            if chosen_func in [1, 2, 3]:
                print("\033[34m{}".format("Chosen function:"), get_func_name(chosen_func))
                print("\033[0m".format(), end='')
                return get_func(chosen_func)
            print("\033[31m{}".format("Error: Invalid input. Choose int number between 1 and 3."))
            print("\033[0m".format(), end='')
        except:
            print("\033[31m{}".format("Error: Invalid input. Choose INT NUMBER between 1 and 3."))
            print("\033[0m".format(), end='')
            pass


def choose_func_with_break():
    while True:
        try:
            print("Choose a function to integrate:")
            for i in [1, 2, 3]:
                print(str(i) + ")", get_break_func_name(i))
            chosen_func = int(input(">>>"))
            if chosen_func in [1, 2, 3]:
                print("\033[34m{}".format("Chosen function:"), get_break_func_name(chosen_func))
                print("\033[0m".format(), end='')
                func, brk = get_break_func(chosen_func)
                return func, brk, chosen_func
            print("\033[31m{}".format("Error: Invalid input. Choose int number between 1 and 3."))
            print("\033[0m".format(), end='')
        except:
            print("\033[31m{}".format("Error: Invalid input. Choose INT NUMBER between 1 and 3."))
            print("\033[0m".format(), end='')
            pass


def get_break_func(num):
    if num == 1:
        return lambda x: 1 / x, 0
    if num == 2:
        return lambda x: x ** 2 if x < 2 else 3 * x, 2
    if num == 3:
        return lambda x: x / abs(x), 0


def get_break_func_name(num):
    if num == 1:
        return "1/x"
    if num == 2:
        return "x^2 given that x < 2, 3x given that х >= 2"
    if num == 3:
        return "sign(x)"


def input_borders():
    while True:
        try:
            print("Enter the lower border of the interval")
            lower = float(input(">>>"))
            print("Enter the upper border of the interval")
            upper = float(input(">>>"))
            print("\033[34m{}".format("Chosen borders:"), "lower:", lower, ";upper", upper)
            print("\033[0m".format(), end='')
            return lower, upper
        except:
            print("\033[31m{}".format("Error: invalid input. Re-try input"))
            print("\033[0m".format(), end='')
            pass


def input_accuracy():
    while True:
        try:
            print("Enter an accuracy that is a multiple of a power of 10")
            e = float(input(">>>"))
            if e > 0 and math.log10(e) == int(math.log10(e)):
                print("\033[34m{}".format("Chosen accuracy:"), e)
                print("\033[0m".format(), end='')
                return e
            print("\033[31m{}".format("Error: Wrong input. Chose float number lower than 0 and that is a multiple of "
                                      "a power of 10"))
            print("\033[0m".format(), end='')
        except:
            print("\033[31m{}".format("Error: Wrong input. Chose FLOAT NUMBER lower than 0 and that is a multiple of "
                                      "a power of 10"))
            print("\033[0m".format(), end='')
            pass


def get_func(num):
    if num == 1:
        return lambda x: x ** 3 + 2.28 * (x ** 2) - 1.934 * x - 3.907
    if num == 2:
        return lambda x: x ** 2 - 3 * x - 2
    if num == 3:
        return lambda x: math.sin(x) - math.cos(x) + 0.2 * x


def get_func_name(num):
    if num == 1:
        return "x^3 + 2.28x^2 - 1.934x - 3.907"
    if num == 2:
        return "x^2 - 3x - 2"
    if num == 3:
        return "sin(x) - cos(x) + 0.2x"


def choose_method():
    while True:
        try:
            print("Choose method:")
            for i in [1, 2, 3, 4]:
                print(str(i) + ")", get_method_name(i))
            chosen_method = int(input(">>>"))
            if chosen_method in [1, 2, 3, 4]:
                print("\033[34m{}".format("Chosen function:"), get_method_name(chosen_method))
                print("\033[0m".format(), end='')
                return chosen_method
            print("\033[31m{}".format("Error: Wrong input. Chose int number between 1 and 4."))
            print("\033[0m".format(), end='')
        except:
            print("\033[31m{}".format("Error: Wrong input. Chose INT NUMBER between 1 and 4."))
            print("\033[0m".format(), end='')
            pass


def choose_method_for_breaks():
    while True:
        try:
            print("Choose method:")
            for i in [1, 2, 3, 4, 5]:
                print(str(i) + ")", get_method_name(i))
            chosen_method = int(input(">>>"))
            if chosen_method in [1, 2, 3, 4, 5]:
                print("\033[34m{}".format("Chosen function:"), get_method_name(chosen_method))
                print("\033[0m".format(), end='')
                return chosen_method
            print("\033[31m{}".format("Error: Wrong input. Chose int number between 1 and 4."))
            print("\033[0m".format(), end='')
        except:
            print("\033[31m{}".format("Error: Wrong input. Chose INT NUMBER between 1 and 4."))
            print("\033[0m".format(), end='')
            pass


def get_method_name(num):
    if num == 1:
        return "Right rectangle method"
    if num == 2:
        return "Left rectangle method"
    if num == 3:
        return "Mid rectangle method"
    if num == 4:
        return "Trapeze method"
    if num == 5:
        return "Simpson's method"


def get_method(num, func, a, b):
    if num == 1:
        return method_right_rectangle(func, a, b)
    if num == 2:
        return method_left_rectangle(func, a, b)
    if num == 3:
        return method_mid_rectangle(func, a, b)
    if num == 4:
        return method_trapeze(func, a, b)
    if num == 5:
        return method_simpson(func, a, b)


# ---methods---
def method_right_rectangle(func, a, b):
    return func(b) * (b - a)


def method_left_rectangle(func, a, b):
    return func(a) * (b - a)


def method_mid_rectangle(func, a, b):
    return func((a + b) / 2) * (b - a)


def method_simpson(func, a, b):
    return ((b - a) / 6) * (func(a) + 4 * func((a + b) / 2) + func(b))


def method_trapeze(func, a, b):
    return ((func(a) + func(b)) / 2) * (b - a)


def main():
    print("\033[31m\033[40m{}".format("Soloviev Artemiy P32151"))
    print("Task option 11")
    print("\033[0m".format())
    mode = choose_func_type()
    k = 1
    if mode == 1:
        func = choose_func()
        method = choose_method()
        a, b = input_borders()
        if a > b:
            k = -1
            a, b = b, a
        accuracy = input_accuracy()
        result, splits, accuracy = simple_integral_calculation(func, method, a, b, accuracy, 2)
        print("result =", round(result * k, int(abs(math.log10(accuracy)))), "; splits =", splits, "error =", accuracy,
              end='')
    else:
        func, brk, chosen_func = choose_func_with_break()
        method = choose_method_for_breaks()
        a, b = input_borders()
        if a > b:
            k = -1
            a, b = b, a
        accuracy = input_accuracy()
        if chosen_func == 1:
            result = second_break_integral_calculation(func, method, a, b, brk, accuracy)
        else:
            result = first_break_integral_calculation(func, method, a, b, brk, accuracy)
        print("result =", round(result*k, int(abs(math.log10(accuracy)))))


if __name__ == '__main__':
    main()
