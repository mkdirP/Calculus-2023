import math
from scipy import linalg

def get_res_arr(x, fun):
	y = []
	for i in range(len(x)):
		y.append(fun(x[i]))
	return x, y

def get_res_fun(a, b, h, fun):
	X = []
	Y = []
	x = a
	while x <= b:
		X.append(x)
		Y.append(fun(x))
		x += h
	return X, Y

def ln(a):
	return math.log(a, math.e)


def square_approx_arr(X, Y):
	sum_xi = 0
	sum_xi_2 = 0
	sum_xi_3 = 0
	sum_xi_4 = 0

	sum_yi = 0
	sum_xi_yi = 0
	sum_xi_2_yi = 0

	for i in range(len(X)):
		sum_xi += X[i]
		sum_xi_2 += X[i]**2
		sum_xi_3 += X[i]**3
		sum_xi_4 += X[i]**4

		sum_yi += Y[i]
		sum_xi_yi += X[i] * Y[i]
		sum_xi_2_yi += X[i] ** 2 * Y[i]

	a, b, c = linalg.solve([[sum_xi_3, sum_xi_2, sum_xi], [sum_xi_4, sum_xi_3, sum_xi_2], [sum_xi_2, sum_xi, len(X)]], [sum_xi_yi, sum_xi_2_yi, sum_yi])

	def new_func(x):
		return a * x ** 2 + b * x + c

	return True, new_func, a, b, c

def square_approx_fun(a, b, h, f):
	transform = get_res_fun(a, b, h, f)
	return square_approx_arr(transform[0], transform[1])

def power_approx_arr(X, Y):
	sum_xi = 0
	sum_xi_2 = 0

	sum_yi = 0
	sum_xi_yi = 0

	for i in range(len(X)): 
		if X[i] <= 0 or Y[i] <= 0:
			return False, False
		sum_xi += ln(X[i])
		sum_xi_2 += ln(X[i]) ** 2

		sum_yi += ln(Y[i])
		sum_xi_yi += ln(X[i]) * ln(Y[i])
	answ = linalg.solve([[sum_xi_2, sum_xi], [sum_xi, len(X)]], [sum_xi_yi, sum_yi])
	a = math.e ** answ[1]
	b = answ[0]

	def new_func(x):
		return a * x **b

	return True, new_func, a, b

def power_approx_fun(a, b, h, f):
	transform = get_res_fun(a, b, h, f)
	return power_approx_arr(transform[0], transform[1])


def log_approx_arr(X, Y):
	sum_xi = 0
	sum_xi_2 = 0

	sum_yi = 0
	sum_xi_yi = 0

	for i in range(len(X)):
		if X[i] <= 0:
			return False, False
		sum_xi += ln(X[i])
		sum_xi_2 += ln(X[i]) ** 2

		sum_yi += Y[i]
		sum_xi_yi += ln(X[i]) * Y[i]
	a, b = linalg.solve([[sum_xi_2, sum_xi], [sum_xi, len(X)]], [sum_xi_yi, sum_yi])

	def new_func(x):
		return a * ln(x) + b
	return True, new_func, a, b

def log_approx_fun(a, b, h, f):
	transform = get_res_fun(a, b, h, f)
	return log_approx_arr(transform[0], transform[1])

def lin_approx_arr(X, Y):
	sum_xi = 0
	sum_xi_2 = 0

	sum_yi = 0
	sum_xi_yi = 0

	for i in range(len(X)):
		sum_xi += X[i]
		sum_xi_2 += X[i] ** 2

		sum_yi += Y[i]
		sum_xi_yi += Y[i] * X[i]

	a, b = linalg.solve([[sum_xi_2, sum_xi], [sum_xi, len(X)]], [sum_xi_yi, sum_yi])

	def new_func(x):
		return a * x + b

	return True, new_func, a, b

def lin_approx_fun(a, b, h, f):
	transform = get_res_fun(a, b, h, f)
	return lin_approx_arr(transform[0], transform[1])


def exp_approx_arr(X, Y):
	sum_xi = 0
	sum_xi_2 = 0

	sum_yi = 0
	sum_xi_yi = 0

	for i in range( len(X)):
		if Y[i] <= 0:
			return False, False
		sum_xi += X[i]
		sum_xi_2 += X[i] ** 2

		sum_yi += ln(Y[i])
		sum_xi_yi += X[i] * ln(Y[i])

	answ = linalg.solve([[sum_xi_2, sum_xi], [sum_xi,  len(X)]], [sum_xi_yi, sum_yi])
	a = math.e ** answ[1]
	b = answ[0]

	def new_func(x):
		return a * math.e**(b*x)
	return True, new_func, a, b

def exp_approx_fun(a, b, h, f):
	transform = get_res_fun(a, b, h, f)
	return exp_approx_arr(transform[0], transform[1])


def cube_approx_arr(X, Y):
	sum_xi = 0
	sum_xi_2 = 0
	sum_xi_3 = 0
	sum_xi_4 = 0
	sum_xi_5 = 0
	sum_xi_6 = 0

	sum_yi = 0
	sum_xi_yi = 0
	sum_xi_2_yi = 0
	sum_xi_3_yi = 0

	for i in range(len(X)):
		sum_xi += X[i]
		sum_xi_2 += X[i] ** 2
		sum_xi_3 += X[i] ** 3
		sum_xi_4 += X[i] ** 4
		sum_xi_5 += X[i] ** 5
		sum_xi_6 += X[i] ** 6

		sum_yi += Y[i]
		sum_xi_yi += X[i] * Y[i]
		sum_xi_2_yi += X[i] ** 2 * Y[i]
		sum_xi_3_yi += X[i] ** 3 * Y[i]

	a, b, c, d = linalg.solve([[sum_xi_6, sum_xi_5, sum_xi_4, sum_xi_3], [sum_xi_5, sum_xi_4, sum_xi_3, sum_xi_2],[sum_xi_4, sum_xi_3, sum_xi_2, sum_xi], [sum_xi_3, sum_xi_2, sum_xi, len(X)]], [sum_xi_3_yi, sum_xi_2_yi, sum_xi_yi, sum_yi])

	def new_func(x):
		return a * x ** 3 + b * x ** 2 + c * x + d

	return True, new_func, a, b, c, d

def cube_approx_fun(a, b, h, f):
	transform = get_res_fun(a, b, h, f)
	return cube_approx_arr(transform[0], transform[1])


