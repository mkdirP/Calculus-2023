import matplotlib.pyplot as plt

plot_area = 2


# отрисовка графиков
def plot_lag_newton(x, f_y, lag_y, newton_y, stirling_y, bessel_y, point_x, point_y):
    if f_y != None:
        plt.plot(x, f_y(x), linewidth=2.0, label="function")
    plt.plot(x, lag_y, linewidth=2.0, label="lagrange")
    plt.plot(x, newton_y, linewidth=2.0, label="newton")
    plt.plot(x, stirling_y, linewidth=2.0, label="stirling")
    plt.plot(x, bessel_y, linewidth=2.0, label="bessel")
    plt.plot(point_x, point_y, '*', linewidth=0, label="points")
    plt.legend()
    plt.grid(True)
    minimum_x = min(point_x)
    minimum_y = min(point_y)
    maximum_x = max(point_x)
    maximum_y = max(point_y)
    plt.xlim(minimum_x - plot_area, maximum_x + plot_area)
    plt.ylim(minimum_y - plot_area, maximum_y + plot_area)
    plt.show()


INPUT = "./input.txt"


# исключение дубликатов координат
def sort_and_delete_dublicates(points):
    points.sort()
    i = 1
    while i < len(points):
        if points[i][0] == points[i - 1][0]:
            points[i - 1] = (points[i - 1][0], (points[i - 1][1] + points[i][1]) / 2)
            points.pop(i)
        else:
            i += 1
    return points


# Получение точек из файла
def get_points_file():
    # Получение точек из файла
    with open(INPUT, 'rt') as file:
        try:
            x = []
            y = []
            for line in file:
                new_row = list(map(float, line.strip().split()))
                if len(new_row) != 2:
                    raise ValueError
                x.append(new_row[0])
                y.append(new_row[1])
            t = [(x[i], y[i]) for i in range(len(x))]
            p = sort_and_delete_dublicates(t)
            x = [p[0] for p in t]
            y = [p[1] for p in t]
        except ValueError:
            print("Неверный формат файла")
            exit()
    return x, y


def get_points_from_func(f, a, b, step):
    x = []
    y = []
    x_now = a
    while x_now <= b:
        x.append(x_now)
        y.append(f(x_now))
        x_now += step
    return x, y


# выбор источника
def ask_input_data():
    mode = 0
    while mode != 1 and mode != 2:
        try:
            mode = int(input("Ведите источник точек.\n Для файла - 1\n Для функции - 2:\n "))
        except Exception:
            print("Неправильный формат. Введите число")
    return mode


def ask_num():
    a = 0
    while True:
        try:
            a = float(input())
            return a
        except Exception:
            print("Неправильный формат. Введите число")
