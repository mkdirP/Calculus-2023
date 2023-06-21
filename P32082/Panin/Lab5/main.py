import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from functions import *
from interpolation import *


def draw(X, Y, f):
    x_interval = np.linspace(min(X)-min(X)/4, max(X)+min(X)/4, 100)
    y_interval = list(map(f, x_interval))
    plt.plot(X, Y, "ro")
    plt.plot(x_interval, y_interval)
    plt.axis([min(x_interval)-min(x_interval)/4, max(x_interval)+max(x_interval)/4, min(min(Y), min(y_interval)) - min((min(Y), min(y_interval)))/4, max(max(Y), max(y_interval)) + max((max(Y), max(y_interval)))/4])
    plt.show()	

# txxF3Euu


while(1):
	inp = input("Choose file or function(file/func):")
	if inp == "file":
		filename = input("Enter file name:")
		file = pd.read_csv(filename)
		Y = file["Y"]
		X = file["X"]
		print(file)
		draw(X, Y, gen_func(lagrange_func, X, Y))
		draw(X, Y, gen_func(newton_func, X, Y))
	elif inp == "func":
		a, b = [int(x) for x in input("Enter interval:").split()]
		h = float(input("Enter h:"))
		if h >= b - a:
			print("Bad h value!")
			continue
		X = []
		while a < b:
			X.append(a)
			a += h
		funcs = [f1, f2, f3, f4, f5, f6]
		i = int(input("Enter functions id(1-6):"))
		Y = get_res_arr(X, funcs[i-1])[1]
		draw(X, Y, gen_func(lagrange_func, X, Y))
		draw(X, Y, gen_func(newton_func, X, Y))
	else:
		print("Bad input!")