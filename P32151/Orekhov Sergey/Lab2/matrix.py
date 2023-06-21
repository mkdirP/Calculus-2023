import numpy as np
from matplotlib import pyplot as plt

def system1():
	print("x^2 + y^2 - 4 = 0")
	print("3x^2 - y = 0")
	eps = float(input("Введите эпсилон:\n").replace(",", "."))


	a = np.arange(-2, 2, 0.01)
	b = np.arange(-10, 10, 0.01)
	t = np.arange(0, 2 * np.pi, 0.01)
	r = 4
	plt.plot(a, a**3 - 1, b, b+6, lw=3)
	plt.axis('equal')


	xp = float(input("Введите X0!\n").replace(",", "."))
	yp = float(input("Введите Y0!\n").replace(",", "."))

	if xp == 0:
		xp = 0.01
	if yp == 0:
		yp = 0.01
	x = 0
	y = 0
	x, y = itersys1(xp, yp, eps)
	print("X:", x, "Y:", y)
	plt.plot(x, y, 'ro')
	plt.show()


def get_one_step_1(x, y):
	return [(x + 1)**0.33, x+6]



def itersys1(x, y, eps):

	step = get_one_step_1(x, y)
	xi = step[0]
	yi = step[1]
	print(xi, yi)

	while abs(x - xi) > eps or abs(y - yi) > eps:
		x = xi
		y = yi
		step = get_one_step_1(x, y)
		xi = step[0]
		yi = step[1]


	x = xi
	y = yi
	return x, y



def system2():
	print("y/(1 + y*y) - 2x = 0")
	print("x/(1+x*x) - 2y = 0")

	eps = float(input("Введите эпсилон:\n").replace(",", "."))

	x = np.linspace(-np.pi, np.pi, 100)
	t = np.linspace(-np.pi / 1000, np.pi / 1000, 100)

	y = 2*x + 2 * x * t * t - t
	z = 2 * x + 2 * x * y * y - y

	fig = plt.figure()
	ax = fig.add_subplot(1, 1, 1)
	ax.spines['left'].set_position('center')
	ax.spines['bottom'].set_position('center')
	ax.spines['right'].set_color('none')
	ax.spines['top'].set_color('none')
	ax.xaxis.set_ticks_position('bottom')
	ax.yaxis.set_ticks_position('left')


	plt.plot(y)
	plt.plot(z)

	plt.show()

	xp = float(input("Введите X0!\n").replace(",", "."))
	yp = float(input("Введите Y0!\n").replace(",", "."))


	if xp == 0:
		xp = 0.01
	if yp == 0:
		yp = 0.01

	x, y = itersys1(xp, yp, eps)
	print("X:", x, "Y:", y)
	plt.plot(x, y, 'ro')
	plt.show()

def get_one_step_2(x, y):
	return [(y/(2*(1+y*y))), (x/(2*(1+x*x)))]


def itersys2(x, y, eps):
	step = get_one_step_2(x, y)
	xi = step[0]
	yi = step[1]
	print(xi, yi)

	while abs(x - xi) > eps or abs(y - yi) > eps:
		x = xi
		y = yi
		step = get_one_step_2(x, y)
		xi = step[0]
		yi = step[1]

	x = xi
	y = yi
	return x, y