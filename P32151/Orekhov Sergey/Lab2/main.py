from matrix import *
from methods import *
from Functions import *
import math

while True:
    inp = input("Выберите уравнение или систему(s1 - система 1, s2 - система 2, f1 - уравнение 1, f2 - уравнение 2, f3 - уравнение 3):\n")

    if inp == "s1":
        system1()
    elif inp == "s2":
        system2()
    elif inp[0] == 'f':
        if inp[1] == '1':
            urav = f1
        elif inp[1] == '2':
            urav = f2
        elif inp[1] == '3':
            urav = f3
        else:
            print("Неправильный ввод")
            continue
        inp1 = input("Выберите метод(хорд - cd, секущих - sc, простой итерации - si)")
        if inp1 == "cd":
            a, b = [float(x) for x in input("Выберите интервал(<a> <b>):").replace(",", ".").split()]
            print(chords(urav, a, b))
        if inp1 == "sc":
            a, b = [float(x) for x in input("Выберите интервал(<a> <b>):").replace(",", ".").split()]
            print(sec(urav, a, b))
        if inp1 == "si":
            a, b = [float(x) for x in input("Выберите интервал(<a> <b>):").replace(",", ".").split()]
            print(simple_iter(urav, a, b))
    else:
        print("Неправильный ввод\n")



