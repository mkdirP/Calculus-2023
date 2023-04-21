import matplotlib.pyplot as plt
import numpy as np
import math

def check_interval(func, a, b):
	print("f(a):%f", func(a))
	print("f(b):%f", func(b))
	if(func(a)*func(b) < 0):
		return True
	else:
		return False


def half_division(func, a, b):

	if(check_interval(func, a, b) == False):
		return "Bad interval!"

	xnpy = np.linspace(a, b, 100)
	ynpy = func(xnpy)
	fig = plt.figure()
	ax = fig.add_subplot(1, 1, 1)
	ax.spines['left'].set_position('center')
	ax.spines['bottom'].set_position('center')
	ax.spines['right'].set_color('none')
	ax.spines['top'].set_color('none')
	ax.xaxis.set_ticks_position('bottom')
	ax.yaxis.set_ticks_position('left')
	plt.plot(xnpy,ynpy, 'g')
	plt.show()

	eps = float(input("Enter epsilon!\n").replace(",", "."))
	x = (a + b)/2

	cur_eps = abs(a-b)
	while(cur_eps > eps):
		x = (a + b)/2
		if func(a) * func(x) > 0 > func(b) * func(x):
			a = x
		elif func(b) * func(x) > 0 > func(a) * func(x):
			b = x
		elif func(x) == 0:
			return x
		else:
			sys.exit("something wrong in the hd method\n")
		cur_eps = abs(a-b)
	return x


def simple_iter(func, a, b):
	# graph somehow

	if(check_interval(func, a, b) == False):
		return "Bad interval!"

	xnpy = np.linspace(a, b, 100)
	ynpy = func(xnpy)
	fig = plt.figure()
	ax = fig.add_subplot(1, 1, 1)
	ax.spines['left'].set_position('center')
	ax.spines['bottom'].set_position('center')
	ax.spines['right'].set_color('none')
	ax.spines['top'].set_color('none')
	ax.xaxis.set_ticks_position('bottom')
	ax.yaxis.set_ticks_position('left')
	plt.plot(xnpy,ynpy, 'g')
	plt.show()		

	eps = float(input("Enter epsilon!\n").replace(",", "."))
	deriv_a = (func(a + eps/100)-func(a))/(eps/100)
	deriv_b = (func(b + eps/100)-func(b))/(eps/100)
	if(deriv_a > deriv_b):
		max_deriv = deriv_a
		xi = a
	else:
		max_deriv = deriv_b
		xi = b
	lamda = -1 / max_deriv
	itercount = 0
	while(abs(xi + lamda * func(xi) - xi) > eps):
		if itercount > 1000:
			return xi + lamda * func(xi)
		xi = xi + lamda * func(xi)
		itercount += 1
	return xi + lamda * func(xi)


def newton(func, a, b):
	# graph somehow

	if(check_interval(func, a, b) == False):
		return "Bad interval!"

	xnpy = np.linspace(a, b, 100)
	ynpy = func(xnpy)
	fig = plt.figure()
	ax = fig.add_subplot(1, 1, 1)
	ax.spines['left'].set_position('center')
	ax.spines['bottom'].set_position('center')
	ax.spines['right'].set_color('none')
	ax.spines['top'].set_color('none')
	ax.xaxis.set_ticks_position('bottom')
	ax.yaxis.set_ticks_position('left')
	plt.plot(xnpy,ynpy, 'g')
	plt.show()		

	eps = float(input("Enter epsilon!\n").replace(",", "."))

	xip = b
	xi = xip - func(xip)/((func(xip + eps/100)-func(xip))/(eps/100))

	while(abs(func(xi)) <= eps):
		tmp = xi
		xi = xip - func(xip)/((func(xip + eps/100)-func(xip))/(eps/100))
		xip = tmp
	return xi
