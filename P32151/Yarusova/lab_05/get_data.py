from math import sin


def get_data():
    input_format = choose_input_format()
    dots = []
    match input_format:
        case 1:
            dots = read_dots()
        case 2:
            dots = read_dots_from_file()
        case 3:
            dots = read_dots_from_function()
    dots.sort()
    method = choose_method()
    checked_dots = check_dots(dots)
    if checked_dots is None:
        return None
    data = {'x': [dot[0] for dot in dots], 'y': [dot[1] for dot in dots]}
    interpolation_dot = choose_interpolation_dot(dots)
    return data, method, interpolation_dot


def choose_input_format():
    print("Choose the input format:")
    print("1. Console (default)")
    print("2. File")
    print("3. Function")
    input_format = int(input())
    if input_format not in [1, 2, 3]:
        print("Wrong input format (default))")
        input_format = 1
    return input_format


def read_dots():
    print("Enter dots in format: x y")
    print("Enter 'stop' to stop entering dots")
    data = []
    while True:
        line = input().strip()
        if line == 'stop':
            if len(data) < 3:
                print("You must enter at least 3 dots")
                continue
            break
        dot = tuple(map(float, line.split()))
        if len(dot) != 2:
            print("You must enter 2 numbers")
            continue
        data.append(dot)
    return data


def read_dots_from_file():
    print("Enter the file name: ")
    file = input()
    f = open(file, 'r')
    data = []
    for line in f:
        if line.strip() == 'stop':
            break
        dot = tuple(map(float, line.strip().split()))
        if len(dot) != 2:
            print("You must enter 2 numbers for each dot")
            return None
        data.append(dot)
    if len(data) < 3:
        print("You must enter at least 3 dots")
        return None
    return data


def read_dots_from_function():
    print("Choose the function: ")
    print("1. y = x^2 (default)")
    print("2. y = 1 / (x^2 + 1)")
    print("3. y = sin(x)")
    input_function = int(input())
    if input_function not in [1, 2, 3]:
        print("Wrong function (default)")
        input_function = 1
    func = lambda x: x ** 2
    match input_function:
        case 2:
            func = lambda x: 1 / (x ** 2 + 1)
        case 3:
            func = lambda x: sin(x)
    print("Enter interval: ")
    print("Enter left border (default -10): ")
    left = float(input())
    print("Enter right border (default 10): ")
    right = float(input())
    if left is None:
        left = -10
    if right is None:
        right = 10
    if left == right:
        print("Left and right borders must be different (default)")
        left, right = -10, 10
    if left > right:
        print("Left border must be less than right border(swap them)")
        left, right = right, left
    print("Enter number of dots (default 10): ")
    number = int(input())
    if number is None or number <= 0:
        print("Number of dots must be positive(default)")
        number = 10
    h = (right - left) / number
    data = [(left + h * i, func(left + h * i)) for i in range(number)]
    return data


def choose_method():
    print("Choose the method:")
    print("1. Lagrange")
    print("2. Newton")
    print("3. Both (default))")
    method = int(input())
    if method not in [1, 2, 3]:
        print("Wrong method (default)")
        method = 3
    return method


def check_dots(dots):
    unique = set()
    i = 0
    for dot in dots:
        if dot[0] in unique:
            print("All x must be different (delete this dot)" + str(dot))
            dots[i][1] = (dots[i - 1][1] + dots[i][1]) / 2
            dots.pop(dot)
        unique.add(dot[0])
        i += 1
    if len(dots) < 3:
        print("You must enter at least 3 unique dots")
        return None
    return dots


def choose_interpolation_dot(dots):
    print("Choose the interpolation dot (default 0): ")
    dot = float(input())
    if dot is None:
        print("Wrong interpolation dot (default)")
        dot = 0
    if dot < dots[0][0] or dot > dots[-1][0]:
        print("Interpolation dot must be in the interval of dots (default)")
        dot = 0
    return dot
