import numexpr as ne

EQUATIONS = {
    1: "y`=(x-y)**2",
    2: "y`=(x-y)**2+y**2",
    3: "y`=sin(x)+y",
    4: "y`=y+(1+x)*y**2"
}

ANSWERS = {
    1: "y=1/(c*exp(2*x)+1/2)+x-1",
    2: "y=1/(2*(c-x))+x/2",
    3: "y=c*exp(x)- sin(x)/2-cos(x)/2",
    4: "y=-(exp(x))/(c+exp(x)*x)"
}

C = {
    1: "с=(-1/2*y+1-1/2*x-1/2)/(exp(2*x)*y-exp(2*x)*x+exp(2*x))",
    2: "c=(1-2*x**2+2*y*x)/(2*(y-x))",
    3: "c=y/exp(x)+sin(x)/(2*exp(x))+cos(x)/(2*exp(x))",
    4: "c=-exp(x)/y-exp(x)*x"
}


def calculateFunction(xi, yi, function_number):
    return float(ne.evaluate(EQUATIONS[function_number].split('=')[1], local_dict={'x': xi, 'y': yi}))


def calculateAnswer(x0, y0, xi, function_number):
    c = calculateC(x0, y0, function_number)
    return float(
        ne.evaluate(ANSWERS[function_number].split('=')[1], local_dict={'x': xi, 'c': c}))


def calculateC(x0, y0, function_number):
    return float(ne.evaluate(C[function_number].split('=')[1], local_dict={'x': x0, 'y': y0}))


METHODS = ['Одношаговый. Усовершенствованный метод Эйлера',
           'Одношаговый. Метод Рунге-Кутта 4-го порядка',
           'Многошаговый. Метод Адамса']
