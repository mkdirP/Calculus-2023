from reader import *
from aprox.dop import *
from aprox import linear
from aprox import logarithm
from aprox import cube
from aprox import square
from aprox import power
from aprox import exponent
import reader
import calculates
import matplotlib.pyplot as plt
import numpy as np

ent = input("Input c - for console, f - for file: ")
if ent == "c":
    print("Enter N:")
    n_str = input()
    n = read_int(n_str)
    print("Enter values:")
    x_str = input()
    y_str = input()
    x_arr, y_arr = read_input_values(x_str, y_str, n)
elif ent == "f":
    with open("input.txt") as inp_f:
        n = read_int(inp_f.readline())
        x_arr, y_arr = read_input_values(inp_f.readline(), inp_f.readline(), n)

else:
    print("Wrong choice")
    exit()

linear = linear.Linear(x_arr, y_arr, n)
cube = cube.Cube(x_arr, y_arr, n)
exponent = exponent.Exponent(x_arr, y_arr, n)
logarithm = logarithm.Logarithm(x_arr, y_arr, n)
power = power.Power(x_arr, y_arr, n)
square = square.Square(x_arr, y_arr, n)
aprox_list = [linear, square, cube, exponent, power, logarithm]
f_out = open("output.txt", "w")

for aproximation in aprox_list:

    aproximation.calculate_sums()
    aproximation.calculate_coeff()
    calculates.calc_phi(aproximation)
    print(aproximation.name)
    f_out.write(aproximation.name + "\n")
    print(aproximation.func_string())
    f_out.write(str(aproximation.func_string()) + "\n")
    print(aproximation.phi_array)
    f_out.write(str(aproximation.phi_array) + "\n")
    print("DM:" + str(calculates.deviation_measure(aproximation)))
    f_out.write("DM:" + str(aproximation.dm) + "\n")
    print("SKO: " + str(calculates.calc_sko(aproximation)))
    f_out.write("SKO: " + str(aproximation.sko) + "\n")
    print(" ")
    f_out.write("\n")
    plt.cla()
    x = np.linspace(x_arr[0], x_arr[-1], 10)
    y = aproximation.func(x)
    plt.title(aproximation.name)
    plt.grid()
    plt.plot(x, y)
    plt.scatter(x_arr, y_arr, color="red")
    plt.show()
max_sko = 100000
best_aprox = ""
coeff = calculates.calc_r(linear)
print("Coeff Pirson: " + str(coeff))
f_out.write("Coeff Pirson: " + str(coeff) + "\n")
for aproximation in aprox_list:
    if aproximation.sko < max_sko:
        max_sko = aproximation.sko
        best_aprox = aproximation.name
print("Best aprox is: " + best_aprox)
f_out.write("Best aprox is: " + best_aprox + "\n")
print("adfs")
# linear.calculate_sums()
# linear.calculate_coeff()
# calculates.calc_phi(linear)
# print(linear.x_array)
# print(linear.y_array)
# print(linear.phi_array)
# print(linear.a, linear.b)
