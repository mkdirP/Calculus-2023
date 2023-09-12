import data_io as data
import functions as func
from calculations import*

functionNum = data.get_function_num()

function = func.get_function(functionNum)

a, b = data.get_interval()

# случай, если а оказывается больше b: интеграл будет равен интегралу с противоположным знаком
mul = 1
if a > b:
    mul = -1
    a, b = b, a

typeMethod = data.ask_method()

error = data.ask_error()

n = data.ask_count_split()

if typeMethod == 1:
    ans, n, err = calc_integral(function, squad_method_left, a, b, error, 2)
elif typeMethod == 2:
    ans, n, err = calc_integral(function, squad_method_right, a, b, error, 2)
elif typeMethod == 3:
    ans, n, err = calc_integral(function, squad_method_mid, a, b, error, 2)
elif typeMethod == 4:
    ans, n, err = calc_integral(function, trapezoid_method, a, b, error, 2)
elif typeMethod == 5:
    ans, n, err = calc_integral(function, simpson_method, a, b, error, 4)

print("Получен ответ: " + str(ans * mul) + " Конечное число разбиения инервала: " + str(n))
