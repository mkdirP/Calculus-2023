from table import *
from functions import *
from approx import *

func_arr = [lin_approx_arr, square_approx_arr, cube_approx_arr, power_approx_arr, log_approx_arr, exp_approx_arr]
names = [["Linear", "phi(x) = ax + b"], ["Square", "phi(x) = a_2 * x^2 + a_1 * x + a_0"], ["Cube", "phi(x) = a_2 * x^2 + a_1 * x + a_0"], ["Power", "phi(x) = ax^b"], ["Logarithm", "phi(x) = ae^{bx}"], ["Exponential", "phi(x) = ae^{bx}"]]


while(1):
	inp = input("read file, or select a function(file/func):")
	if inp == "file":
		fname = input("file name:");
		fl = pd.read_csv(fname);
		generate_table(fl["X"], fl["Y"], func_arr, names).to_csv("answ.csv")
	elif inp == "func":
		inp2 = input("select function(f1, f2, f3, f4):")
		if inp2 == "f1":
			a, b = [int(x) for x in input("Enter interval:").split()]
			h = float(input("Enter h:"))
			if h <= a - b:
				print("take a smaller h")
				continue
			generate_table_handler(a, b, h, f1, func_arr, names).to_csv("answer.csv")
		elif inp2 == "f2":
			a, b = [int(x) for x in input("Enter interval:").split()]
			h = float(input("Enter h:"))
			if h <= a - b:
				print("take a smaller h")
				continue
			generate_table_handler(a, b, h, f1, func_arr, names).to_csv("answer.csv")
		elif inp2 == "f3":
			a, b = [int(x) for x in input("Enter interval:").split()]
			h = float(input("Enter h:"))
			if h <= a - b:
				print("take a smaller h")
				continue
			generate_table_handler(a, b, h, f1, func_arr, names).to_csv("answer.csv")
		elif inp2 == "f4":
			a, b = [int(x) for x in input("Enter interval:").split()]
			h = float(input("Enter h:"))
			if h <= a - b:
				print("take a smaller h")
				continue
			generate_table_handler(a, b, h, f1, func_arr, names).to_csv("answer.csv")
	else:
		print("wrong input!")
