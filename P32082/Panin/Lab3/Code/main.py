from methods import *
from functions import *
import math


while 1:
	inp1 = input("Wich method do you want to see? (s(simpson), t(trapeze), c(cell))")
	if inp1 == "s":
		inp2 = int(input("Which function do you want to integrate?(1, 2, 3)"))
		if inp2 == 1:
			simpson_method(f1)
		elif inp2 == 2:
			simpson_method(f2)
		elif inp2 == 3:
			simpson_method(f3)
		else:
			print("wrong input!")
	elif inp1 == "t":
		inp2 = int(input("Which function do you want to integrate?(1, 2, 3)"))
		if inp2 == 1:
			simpson_method(f1)
		elif inp2 == 2:
			simpson_method(f2)
		elif inp2 == 3:
			simpson_method(f3)
		else:
			print("wrong input!")
	elif inp1 == "c":
		inp2 = int(input("Which function do you want to integrate?(1, 2, 3)"))
		if inp2 == 1:
			cell_method(f1)
		elif inp2 == 2:
			cell_method(f2)
		elif inp2 == 3:
			cell_method(f3)
		else:
			print("wrong input!")
	else:
		print("wrong input!")