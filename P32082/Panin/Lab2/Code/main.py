from matrix import *
from methods import *
from functions import *
import math


while True:
	inp = input("Enter command(s1 - system 1, s2 - system 2, f1 - function 1, f2 - function 2, f3 - function 3):\n")

	if(inp == "s1"):
		system1()
	elif(inp == "s2"):
		system2()
	elif inp == "f1":
		inp1 = input("Select method(half division - hd, Newthon - n, simple iteration - si)")
		if inp1 == "hd":
			a, b = [float(x) for x in input("Your interval(<a> <b>):").replace(",",".").split()]				
			print(half_division(f1, a, b))
		if inp1 == "n":
			a, b = [float(x) for x in input("Your interval(<a> <b>):").replace(",",".").split()]
			print(newton(f1, a, b))
		if inp1 == "si":
			a, b = [float(x) for x in input("Your interval(<a> <b>):").replace(",",".").split()]
			print(simple_iter(f1, a, b))

	elif inp == "f2":
		inp1 = input("Select method(half division - hd, Newthon - n, simple iteration - si)")
		if inp1 == "hd":
			a, b = [float(x) for x in input("Your interval(<a> <b>):").replace(",",".").split()]				
			print(half_division(f2, a, b))

		if inp1 == "n":
			a, b = [float(x) for x in input("Your interval(<a> <b>):").replace(",",".").split()]
			print(newton(f2, a, b))
		if inp1 == "si":
			a, b = [float(x) for x in input("Your interval(<a> <b>):").replace(",",".").split()]
			print(simple_iter(f2, a, b))


	elif inp == "f3":
		inp1 = input("Select method(half division - hd, Newthon - n, simple iteration - si)")
		if inp1 == "hd":
			a, b = [float(x) for x in input("Your interval(<a> <b>):").replace(",",".").split()]				
			print(half_division(f3, a, b))
		if inp1 == "n":
			a, b = [float(x) for x in input("Your interval(<a> <b>):").replace(",",".").split()]
			print(newton(f3, a, b))
		if inp1 == "si":
			a, b = [float(x) for x in input("Your interval(<a> <b>):").replace(",",".").split()]
			print(simple_iter(f3, a, b))
	else:
		print("wrong input!\n")


		
