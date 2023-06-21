import math

def f1(x):
	if(x <= 0):
		return 0
	return math.log(x, 2) + math.log(x, 10)

def f2(x):
	return x + 24;

def f3(x):
	return x**2 + x * 2 + 8

def f4(x):
	return math.e ** (x ** 2 - x + 4)