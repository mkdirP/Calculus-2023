

def runge_rule(ih, ihdiv2, k):
	d = (abs(ihdiv2-ih))/(2**k-1)
	print("Runge rule: i - i_(h/2) = ", d)


def cell_method(f):
	a, b = [float(x) for x in input("Your interval(<a> <b>):").replace(",",".").split()]
	n = int(input("Enter N: "))
	side = [float(x) for x in input("Enter center:").replace(",",".").split()]
	print("Answ: ", math_cell_method(f, a, b, n, side))
	runge_rule(math_cell_method(f, a, b, n, side), math_cell_method(f, a, b, n*2, side), 2)


def math_cell_method(f, a, b, n, side):
	h = (b - a)/n
	answ = 0

	if side == "center":
		a += h /2 
	elif side == "right":
		a += h

	while a < b and n >= 1:
		answ += f(a)
		a += h
		n -= 1
	answ *= h
	return answ

def simpson_method(f):
	a, b = [float(x) for x in input("Your interval(<a> <b>):").replace(",",".").split()]
	n = int(input("Enter N: "))
	print("Answ: ", math_simpson_method(f, a, b, n))	
	runge_rule(math_simpson_method(f, a, b, n), math_simpson_method(f, a, b, n)/2, 4)

def math_simpson_method(f, a, b, n):
	if n % 2:
		n += 1
	h = (b - a)/n

	answ = f(a) + f(b)
	a += h

	for i in range(1, n):
		if not(i % 2):
			answ += 2 * f(a)
		elif i % 2:
			answ += 4 * f(a)
		a += h
	return answ * h / 3

def trapeze_method(f):
	a, b = [float(x) for x in input("Your interval(<a> <b>):").replace(",",".").split()]
	n = int(input("Enter N: "))
	print("Answ: ", math_trapeze_method(f, a, b, n))
	runge_rule(math_trapeze_method(f, a, b, n), math_trapeze_method(f, a, b, n*2), 2)

def math_trapeze_method(f, a, b, n):
	h = (b - a)/h
	answ = (f(a) + f(b))/2
	a += h
	n -= 1

	while a < b and n >= 1:
		answ += f(a)
		a += h
		n -= 1
	answ *= h
	return answ