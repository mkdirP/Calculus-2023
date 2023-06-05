import math

import numpy as np
import matplotlib.pyplot as plt

input_func = lambda x: (3*x)/(x**4 + 3)

INPUT = "./input.txt"


def get_points_func(func, a, b, step):
    points = []
    iteration = a
    while iteration <= b:
        try:
            points.append([iteration, func(iteration)])
        except Exception:
            print(f"Нельзя найти точку от {round(iteration, 3)}")
        iteration += step
        iteration = round(iteration, 3)
    return points


def calc_system(array, n):
    max_iterations = 100000
    epsilon = 0.00001
    vector_old_ans = [0] * n
    vector_ans = [0] * n
    difference = epsilon + 1
    num = 0
    found_answer = True
    errors = [0] * n

    while difference > epsilon:
        for i in range(n):
            sum = 0
            for j in range(n):
                if i != j:
                    sum += array[i][j] / array[i][i] * vector_ans[j]
            vector_ans[i] = array[i][n] / array[i][i] - sum
        for i in vector_ans:
            if i == None or i == math.inf or i == -math.inf:
                print("Значения расходятся, невозможно найти ответ")
                found_answer = False
                exit(0)

        max_difference = 0.0
        for i in range(n):
            if abs(vector_old_ans[i] - vector_ans[i]) > max_difference:
                max_difference = abs(vector_old_ans[i] - vector_ans[i])
        difference = max_difference
        for i in range(n):
            vector_old_ans[i] = vector_ans[i]
        num += 1
        if (num >= max_iterations):
            print("Не удалось получить ответ за максимальное количество итераций")
            found_answer = False
            break
    return vector_ans


# Линейная аппроксимация
def linear_approximate(points):
    n = len(points)

    summ_x = 0
    for i in range(n):
        summ_x += points[i][0]

    summ_x_sqd = 0
    for i in range(n):
        summ_x_sqd += points[i][0] ** 2

    summ_y = 0
    for i in range(n):
        summ_y += points[i][1]

    summ_x_y = 0
    for i in range(n):
        summ_x_y += points[i][0] * points[i][1]

    # коэффициент корреляции Пирсона
    mid_x = summ_x / n
    mid_y = summ_y / n
    # числитель
    summ_1 = 0
    for i in range(n):
        summ_1 += (points[i][0] - mid_x) * (points[i][1] - mid_y)
    # знаменатель (суммы 2 и 3)
    summ_2 = 0
    for i in range(n):
        summ_2 += (points[i][0] - mid_x) ** 2
    summ_3 = 0
    for i in range(n):
        summ_3 += (points[i][1] - mid_y) ** 2

    try:
        r = (summ_1) / (math.sqrt(summ_2 * summ_3))
        print(f"Коэффициент корреляции Пирсона равен: {round(r, 3)}")
    except Exception:
        print("Не получилось посчитать коэффициент корреляции Пирсона")
    ans = calc_system([[summ_x_sqd, summ_x, summ_x_y], [summ_x, n, summ_y]], 2)

    result_func = lambda x: ans[0] * x + ans[1]

    str_result_func = f"{round(ans[0], 3)}x + {round(ans[1], 3)}"

    # среднеквадратичное отклонение
    errors = [(points[i][1] - result_func(points[i][0])) ** 2 for i in range(n)]
    mid_sqd_err = math.sqrt(sum(errors) / n)

    return result_func, str_result_func, errors, mid_sqd_err


# Квадратичная аппроксимация
def squad_approximate(points):
    n = len(points)
    summ_x = 0
    for i in range(n):
        summ_x += points[i][0]

    summ_x_sqd = 0
    for i in range(n):
        summ_x_sqd += points[i][0] ** 2

    summ_x_qub = 0
    for i in range(n):
        summ_x_qub += points[i][0] ** 3

    summ_x_forth = 0
    for i in range(n):
        summ_x_forth += points[i][0] ** 4

    summ_y = 0
    for i in range(n):
        summ_y += points[i][1]

    summ_x_y = 0
    for i in range(n):
        summ_x_y += points[i][0] * points[i][1]

    summ_x_sqd_y = 0
    for i in range(n):
        summ_x_sqd_y += (points[i][0] ** 2) * points[i][1]

    system = [
        [n, summ_x, summ_x_sqd, summ_y],
        [summ_x, summ_x_sqd, summ_x_qub, summ_x_y],
        [summ_x_sqd, summ_x_qub, summ_x_forth, summ_x_sqd_y]
    ]

    ans = calc_system(system, 3)

    result_func = lambda x: ans[2] * (x ** 2) + ans[1] * x + ans[0]

    str_result_func = f"{round(ans[2], 3)}x^2 + {round(ans[1], 3)}x + {round(ans[0], 3)}"

    # СКО
    errors = [(points[i][1] - result_func(points[i][0])) ** 2 for i in range(n)]
    mid_sqd_err = math.sqrt(sum(errors) / n)

    return result_func, str_result_func, errors, mid_sqd_err


# Кубическая аппроксимация
def qub_approximate(points):
    n = len(points)

    summ_x = 0
    for i in range(n):
        summ_x += points[i][0]

    summ_x_sqd = 0
    for i in range(n):
        summ_x_sqd += points[i][0] ** 2

    summ_x_qub = 0
    for i in range(n):
        summ_x_qub += points[i][0] ** 3

    summ_x_forth = 0
    for i in range(n):
        summ_x_forth += points[i][0] ** 4

    summ_x_fifth = 0
    for i in range(n):
        summ_x_fifth += points[i][0] ** 5

    summ_x_six = 0
    for i in range(n):
        summ_x_six += points[i][0] ** 6

    summ_y = 0
    for i in range(n):
        summ_y += points[i][1]

    summ_x_y = 0
    for i in range(n):
        summ_x_y += points[i][0] * points[i][1]

    summ_x_sqd_y = 0
    for i in range(n):
        summ_x_sqd_y += (points[i][0] ** 2) * points[i][1]

    summ_x_cub_y = 0
    for i in range(n):
        summ_x_cub_y += (points[i][0] ** 3) * points[i][1]

    system = [
        [n, summ_x, summ_x_sqd, summ_x_qub, summ_y],
        [summ_x, summ_x_sqd, summ_x_qub, summ_x_forth, summ_x_y],
        [summ_x_sqd, summ_x_qub, summ_x_forth, summ_x_fifth, summ_x_sqd_y],
        [summ_x_qub, summ_x_forth, summ_x_fifth, summ_x_six, summ_x_cub_y]
    ]

    ans = calc_system(system, 4)

    result_func = lambda x: ans[3] * (x ** 3) + ans[2] * (x ** 2) + ans[1] * x + ans[0]

    str_result_func = f"{round(ans[3], 3)}x^3 + {round(ans[2], 3)}x^2 + {round(ans[1], 3)}x + {round(ans[0], 3)}"

    # СКО
    errors = [(points[i][1] - result_func(points[i][0])) ** 2 for i in range(n)]
    mid_sqd_err = math.sqrt(sum(errors) / n)

    return result_func, str_result_func, errors, mid_sqd_err


# Степенная аппроксимация
def degree_approximate(input_points):
    points = []

    # добавляем в массив только те точки, которые подходят по ОДЗ логарифма
    for i in input_points:
        if i[1] > 0 and i[0] > 0:
            points.append(i)

    # if len(points) < 2:, но это будет неидеальная аппроксимация
    if len(points) != len(input_points):
        return None, None, None, None

    n = len(points)
    summ_x = 0
    for i in range(n):
        summ_x += math.log(points[i][0])

    summ_x_sqd = 0
    for i in range(n):
        summ_x_sqd += math.log(points[i][0]) ** 2

    summ_y = 0
    for i in range(n):
        summ_y += math.log(points[i][1])

    summ_x_y = 0
    for i in range(n):
        summ_x_y += math.log(points[i][0]) * math.log(points[i][1])

    try:
        ans = calc_system([[summ_x_sqd, summ_x, summ_x_y], [summ_x, n, summ_y]], 2)
    except Exception:
        return None, None, None, None
    result_func = lambda x: np.exp(ans[1]) * (x ** ans[0])

    str_result_func = f"{round(math.exp(ans[1]), 3)}x^{round(ans[0], 3)}"

    # СКО
    errors = [(points[i][1] - result_func(points[i][0])) ** 2 for i in range(n)]
    mid_sqd_err = math.sqrt(sum(errors) / n)

    return result_func, str_result_func, errors, mid_sqd_err


# экспоненциальная аппроксимация
def exp_approximate(input_points):
    points = []

    for i in input_points:
        if i[1] > 0:
            points.append(i)

    # if len(points) < 2:, но это будет неидеальная аппроксимация
    if len(points) != len(input_points):
        return None, None, None, None

    n = len(points)
    summ_x = 0
    for i in range(n):
        summ_x += points[i][0]

    summ_x_sqd = 0
    for i in range(n):
        summ_x_sqd += points[i][0] ** 2

    summ_y = 0
    for i in range(n):
        summ_y += math.log(points[i][1])

    summ_x_y = 0
    for i in range(n):
        summ_x_y += points[i][0] * math.log(points[i][1])
    try:
        ans = calc_system([[summ_x_sqd, summ_x, summ_x_y], [summ_x, n, summ_y]], 2)
    except Exception:
        return None, None, None, None
    result_func = lambda x: np.exp(ans[1]) * np.exp(ans[0] * x)

    str_result_func = f"{round(math.exp(ans[1]), 3)}e^{round(ans[0], 3)}*x"
    # СКО
    errors = [(points[i][1] - result_func(points[i][0])) ** 2 for i in range(n)]
    mid_sqd_err = math.sqrt(sum(errors) / n)

    return result_func, str_result_func, errors, mid_sqd_err


# Логарифмическая аппроксимация
def ln_approximate(input_points):
    points = []

    for i in input_points:
        if i[0] > 0:
            points.append(i)

    # if len(points) < 2:, но это будет неидеальная аппроксимация
    if len(points) != len(input_points):
        return None, None, None, None

    n = len(points)

    summ_x = 0
    for i in range(n):
        summ_x += math.log(points[i][0])

    summ_x_sqd = 0
    for i in range(n):
        summ_x_sqd += math.log(points[i][0]) ** 2

    summ_y = 0
    for i in range(n):
        summ_y += points[i][1]

    summ_x_y = 0
    for i in range(n):
        summ_x_y += math.log(points[i][0]) * points[i][1]

    try:
        ans = calc_system([[summ_x_sqd, summ_x, summ_x_y], [summ_x, n, summ_y]], 2)
    except Exception:
        return None, None, None, None
    result_func = lambda x: ans[0] * np.log(x) + ans[1]

    str_result_func = f"{round(ans[0], 3)} ln(x) + {round(ans[1], 3)}"

    # СКО
    errors = [(points[i][1] - result_func(points[i][0])) ** 2 for i in range(n)]
    mid_sqd_err = math.sqrt(sum(errors) / n)

    return result_func, str_result_func, errors, mid_sqd_err


def input_file():
    # Получение точек из файла
    with open(INPUT, 'rt') as file:
        try:
            points = []
            for line in file:
                new_row = list(map(float, line.strip().split()))
                if len(new_row) != 2:
                    raise ValueError
                points.append(new_row)
        except ValueError:
            print("Неверный формат файла")
            exit()
    return points


def input_console():
    n = 0
    while n <= 0:
        try:
            n = int(input("Ведите количество точек, которые хотите ввести: "))
        except Exception:
            print("Введите число")

    points = []
    print("Введите точки в формате \"x y\": ")
    while len(points) != n:
        try:
            for i in range(n):
                points.append(list(map(float, input().strip().split())))
                if len(points[i]) != 2:
                    raise ValueError
        except ValueError:
            print("Неправильный формат ввода")
            exit()
    return points


def ask_input_data():
    mode = 0
    while mode != 1 and mode != 2 and mode != 3:
        try:
            mode = int(input("Ведите источник точек. Для файла: 1, для консоли: 2, готовая функция(из задания): 3: "))
        except Exception:
            print("Введите число")
    return mode


def draw_plot(points, lin_f, sqd_f, qub_f, exp_f, log_f, deg_f):
    minimum_x = 0
    maximum_x = 0

    minimum_y = 0
    maximum_y = 0

    points_x = []
    points_y = []

    for i in points:
        maximum_x = max(i[0], maximum_x)
        minimum_x = min(i[0], minimum_x)
        maximum_y = max(i[1], maximum_y)
        minimum_y = min(i[1], minimum_y)
        points_x.append(i[0])
        points_y.append(i[1])

    x = np.linspace(minimum_x - 0.5, maximum_x + 0.5, 10000)

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    ax.plot(x, lin_f(x), "r", linewidth=2.0, label="linear")
    ax.plot(x, sqd_f(x), "g", linewidth=2.0, label="squad")
    ax.plot(x, qub_f(x), "b", linewidth=2.0, label="cube")
    if exp_f is not None:
        ax.plot(x, exp_f(x), "pink", linewidth=2.0, label="exp")
    x = np.linspace(0.000001, maximum_x + 0.5, 10000)
    if log_f is not None:
        ax.plot(x, log_f(x), "darkred", linewidth=2.0, label="log")
    if deg_f is not None:
        ax.plot(x, deg_f(x), "purple", linewidth=2.0, label="deg")
    ax.legend()
    ax.plot(points_x, points_y, linewidth=0 ,marker="o", markersize=5, markeredgecolor="black", markerfacecolor="black")

    ax.set(xlim=(minimum_x - 0.5, maximum_x + 0.5), xticks=np.arange(minimum_x, maximum_x, 0.5),
           ylim=(minimum_y - 0.5, maximum_y + 0.5), yticks=np.arange(minimum_y, maximum_y, 0.5))

    plt.show()


def main():
    print("\033[31m\033[40m{}".format("Soloviev Artemiy P32151"))
    print("Task option 8")
    print("\033[0m".format())
    mode = ask_input_data()

    if mode == 1:
        points = input_file()
    elif mode == 2:
        points = input_console()
    else:
        points = get_points_func(input_func, -2, 0, 0.2)

    print(f"Полученные точки: {points}")
    print()
    linear_func, linear_str_func, linear_err, linear_squad_err = linear_approximate(points)
    print(f"Линейной аппроксимацией получена функция: {linear_str_func}, S = {round(sum(linear_err), 3)}, sigma = {round(linear_squad_err, 3)}")
    print()
    squad_func, squad_str_func, squad_err, squad_squad_err = squad_approximate(points)
    print(f"Квадратичной аппроксимацией получена функция: {squad_str_func}, S = {round(sum(squad_err), 3)}, sigma = {round(squad_squad_err, 3)}")
    print()
    cub_func, cub_str_func, cub_err, cub_squad_err = qub_approximate(points)
    print(f"Кубической аппроксимацией получена функция: {cub_str_func}, S = {round(sum(cub_err), 3)}, sigma = {round(cub_squad_err, 3)}")
    print()
    exp_func, exp_str_func, exp_err, exp_squad_err = exp_approximate(points)
    if exp_func is None:
        print("Нет ни одной точки в области определения экспоненциальной функции")
        exp_squad_err = math.inf
    else:
        print(f"Экспоненциальной аппроксимацией получена функция: {exp_str_func}, S = {round(sum(exp_err), 3)}, sigma = {round(exp_squad_err, 3)}")
    print()
    log_func, log_str_func, log_err, log_squad_err = ln_approximate(points)
    if log_func is None:
        print("Нет ни одной точки в области определения логарифмический функции")
        log_squad_err = math.inf
    else:
        print(
            f"Логарифмической аппроксимацией получена функция: {log_str_func}, S = {round(sum(log_err), 3)}, sigma = {round(log_squad_err, 3)}")
    print()
    deg_func, deg_str_func, deg_err, deg_squad_err = degree_approximate(points)
    if deg_func is None:
        print("Нет ни одной точки в области опредения степенной функции")
        deg_squad_err = math.inf
    else:
        print(
            f"Степенной апроксимацией получена функция: {deg_str_func}, S = {round(sum(deg_err), 3)}, sigma = {round(deg_squad_err, 3)}")
    print()

    min_r = min(linear_squad_err, squad_squad_err, cub_squad_err, exp_squad_err, log_squad_err, deg_squad_err)

    print(f"Минимальное среднеквадратичное отклонение: {round(min_r, 3)}")
    if min_r == linear_squad_err:
        print("Лучшая аппроксимация: линейная")
    elif min_r == squad_squad_err:
        print("Лучшая аппроксимация: квадратичная")
    elif min_r == cub_squad_err:
        print("Лучшая аппроксимация: кубическая")
    elif min_r == exp_squad_err:
        print("Лучшая аппроксимация: экспоненциальная")
    elif min_r == log_squad_err:
        print("Лучшая аппроксимация: логарфимическая")
    elif min_r == deg_squad_err:
        print("Лучшая аппроксимация: степенная")

    draw_plot(points, linear_func, squad_func, cub_func, exp_func, log_func, deg_func)


if __name__ == '__main__':
    main()