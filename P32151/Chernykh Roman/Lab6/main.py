import matplotlib.pyplot as plt
from function import *
from calculations import *
from prettytable import PrettyTable


def draw_plot(runge, adams, euler, x_0, y_0):
    x = [a[0] for a in runge]
    y = [a[1] for a in runge]
    plt.plot(x, y, label="Runge Kutt Method")
    x = [a[0] for a in adams]
    y = [a[1] for a in adams]
    plt.plot(x, y, label="Adams Method")
    x = [a[0] for a in euler]
    y = [a[1] for a in euler]
    plt.plot(x,y,label="lyutiy euler")
    plt.plot(x_0, y_0, marker="o", linewidth=0, label="Solution")
    plt.legend()
    plt.grid(True)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()


def float_input(str):
    while True:
        try:
            num = float(input(str))
            return num
        except Exception:
            print("Введите число")


def choose_func():
    while True:
        for i in range(1, 5):
            print(i, ")", get_str_func(i))
        try:
            func_number = int(input("Выберите функцию (1-4): "))
            if func_number in range(1, 5):
                print("Выбранная функция:", get_str_func(func_number))
                return get_func(func_number)
        except:
            print("Введите целое число от 1 до 4")


def main():
    func = choose_func()
    while True:
        x_0 = float_input("Введите x0: ")
        y_0 = float_input("Введите y0: ")
        a = float_input("Введите левую границу (a): ")
        b = float_input("Введите правую границу (b): ")
        while True:
            h = float_input("Введите h: ")
            if h > 0:
                break
            print("Шаг должен быть больше 0!!")

        while True:
            e = float_input("Введите e: ")
            if e > 0:
                break
            print("e должно быть больше 0!!!")

        if x_0 <= b:
            ansR = rungeKutt_method(func, a, b, x_0, y_0, h, e)
            ansA = adams_method(func, a, b, x_0, y_0, h, e)
            ansE = lyutiy_eulers_method(func, a, b, x_0, y_0, h, e)
            th = ["x", "y_r", "y_a", "y_correct"]
            table = PrettyTable(th)
            if len(ansR) < len(ansA):
                if len(ansE) < len(ansR):
                    for i in range(len(ansR)):
                        for j in range(i, len(ansE)):
                            if (ansE[j][0] >= ansR[i][0]):
                                y_correct = 0.5 * (math.exp(ansA[i][0]) - math.cos(ansA[i][0]) - math.sin(ansA[i][0]))
                                td = [round(ansR[i][0], 3), round(ansR[i][1], 3), round(ansA[j][1], 3), round(y_correct, 3)]
                                table.add_row(td)
                                break
                else:
                    for i in range(len(ansR)):
                        for j in range(i, len(ansA)):
                            if (ansA[j][0] >= ansR[i][0]):
                                y_correct = 0.5 * (math.exp(ansA[i][0]) - math.cos(ansA[i][0]) - math.sin(ansA[i][0]))
                                td = [round(ansR[i][0], 3), round(ansR[i][1], 3), round(ansA[j][1], 3), round(y_correct, 3)]
                                table.add_row(td)
                                break
            else:
                if len(ansE) < len(ansR):
                    for i in range(len(ansR)):
                        for j in range(i, len(ansE)):
                            if (ansE[j][0] >= ansA[i][0]):
                                y_correct = 0.5 * (math.exp(ansA[i][0]) - math.cos(ansA[i][0]) - math.sin(ansA[i][0]))
                                td = [round(ansR[i][0], 3), round(ansR[i][1], 3), round(ansA[j][1], 3), round(y_correct, 3)]
                                table.add_row(td)
                                break
                else:
                    for i in range(len(ansA)):
                        for j in range(i, len(ansR)):
                            if (ansR[j][0] >= ansA[i][0]):
                                y_correct = 0.5 * (math.exp(ansR[i][0]) - math.cos(ansR[i][0]) - math.sin(ansR[i][0]))
                                td = [round(ansA[i][0], 3), round(ansR[j][1], 3), round(ansA[i][1], 3), round(y_correct, 3)]
                                table.add_row(td)
                                break
            print(table)
            print("Метод Рунге-Кута:")
            th = ["x", "y_r"]
            table = PrettyTable(th)
            for i in range(len(ansR)):
                td = [round(ansR[i][0], 3), round(ansR[i][1], 3)]
                table.add_row(td)
            print(table)
            print("Метод Адамса:")
            th = ["x", "y_a"]
            table = PrettyTable(th)
            print("\033[0m".format(), end='')
            for i in range(len(ansA)):
                td = [round(ansA[i][0], 3), round(ansA[i][1], 3)]
                table.add_row(td)
            print(table)
            print("Усовершенствованный метод Эйлера:")
            th = ["x", "y_r"]
            table = PrettyTable(th)
            for i in range(len(ansE)):
                td = [round(ansE[i][0], 3), round(ansE[i][1], 3)]
                table.add_row(td)
            print(table)
            draw_plot(ansR, ansA,ansE, x_0, y_0)
            break
        else:
            print("Введите a < x0 < b")


main()