import math

def get_res_arr(X, fun):
	Y = []
	for i in range(len(X)):
		Y.append(fun(X[i]))
	return X, Y

def get_res_fun(a, b, h, fun):
	X, Y = []
	x = a
	while x <= b:
		X.append(x)
		Y.append(new_funcx)
		x += h
	return X, Y

def gen_func(meth, X, Y):
	def f(x):
		answ = (meth(x, X, Y))
		return answ
	return f

def newton_f_k(X, Y):
	if len(X) == 1:
		return Y[0]
	else:
		f_left = newton_f_k(X[1:].copy(), Y[1:].copy())
		f_right = newton_f_k(X[:-1].copy(), Y[:-1].copy())
		x_left = X[-1]
		x_right = X[0]
		return (f_left - f_right)/(x_left-x_right)

def newton_func(x, X, Y):
	X = list(X)
	Y = list(Y)
	n = 0
	for i in range(1, len(X)):
		sum = (newton_f_k(X[:i].copy(), Y[:i].copy()))
		for j in range(i-1):
			sum *= (x - (X[j]))
		n += sum
	return n


def lagrange_func(x, X, Y):
	sum = 0
	for i in range(len(X)):
		l = 1
		for j in range(len(X)):
			if j == i:
				continue
			l *= ((x-X[j])/(X[i]-X[j]))
		l *= Y[i]
		sum += l
	return sum