import numpy as np
from matplotlib import pyplot as plt

def system1():
	print("x^2 + y^2 - 4 = 0")
	print("3x^2 - y = 0")
	eps = float(input("Enter epsilon!\n").replace(",", "."))


	a = np.arange(-2, 2, 0.01)
	t = np.arange(0, 2 * np.pi, 0.01)
	r = 4
	plt.plot(a, 3 * a * a, r * np.sin(t), r * np.cos(t), lw=3)
	plt.axis('equal')
	plt.show()

	xp = float(input("Enter X0!\n").replace(",", "."))
	yp = float(input("Enter Y0!\n").replace(",", "."))

	if xp == 0:
		xp = 0.01
	if yp == 0:
		yp = 0.01

	itersys1(xp, yp, eps)


def get_matr1(x, y):
	return [[2 * x, 2 * y], [-6 * x, 1], [4 - x * x - y * y, 3 * x * x - y]]

def itersys1(x, y, eps):
	dx, dy = np.linalg.solve(get_matr1(x, y)[0:2], get_matr1(x, y)[2])
	xi = x + dx
	yi = y + dy

	while(abs(x - xi) > eps or abs(y - yi) > eps):
		itersys1(xi, yi, eps)
		return

	x = xi
	y = yi
	print("X:", x, "Y:", y)


def system2():
	print("y/(1 + y*y) - 2x = 0")
	print("x/(1+x*x) - 2y = 0")

	eps = float(input("Enter epsilon!\n").replace(",", "."))

	x = np.linspace(-np.pi, np.pi, 100)
	t = np.linspace(-np.pi / 1000, np.pi / 1000, 100)	

	y = 2*x + 2 * x * t * t -t
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

	xp = float(input("Enter X0!\n").replace(",", "."))
	yp = float(input("Enter Y0!\n").replace(",", "."))


	if xp == 0:
		xp = 0.01
	if yp == 0:
		yp = 0.01

	itersys2(xp, yp, eps)

def get_matr2(x, y):
	 return [[2 + 2 * y * y, 4 * x * y - 1],[4 * x * y - 1, 2 + 2 * x * x], [-2 * x - 2 * x * y * y + y, -2 * y - 2 * y * x * x + x]] 


def itersys2(x, y, eps):
	dx, dy = np.linalg.solve(get_matr2(x, y)[0:2], get_matr2(x, y)[2])
	xi = x + dx
	yi = y + dy

	while(abs(x - xi) > eps or abs(y - yi) > eps):
		itersys2(xi, yi, eps)
		return

	print("X:", xi, " Y:", yi)
	return