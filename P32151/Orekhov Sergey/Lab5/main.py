from interpolation.lagrange import *
from interpolation.newton import *
from system_util.IO import *
from system_util.stats import *
from functions.functions_lib import *

user_input = input("Enter 'file' or 'prep' or 'in'\n")
if user_input == "file":
    df = read_file(input("Enter link\n"))
    Y = df["Y"]
    X = df["X"]
    if(len(X) != len(set(X))):
        sys.exit("Repeat of X")
    x = enter_float("Enter x: ")
    lagr = function_generator(lagrange_function, X, Y)(x)
    newt = function_generator(newton_function, X, Y)(x)
    print("Lagrange = " + str(lagr))
    print("Newton = " + str(newt))
    print(df)
    draw_one_array_one_function(X, Y, function_generator(lagrange_function, X, Y))
    draw_one_array_one_function(X, Y, function_generator(newton_function, X, Y))

if user_input == "prep":
    x = enter_float("Enter x\n")
    a, b = enter_interval()
    h = enter_float("Enter h")
    if h >= b - a:
        sys.exit("take smaller h")
    X = []
    while a < b:
        X.append(a)
        a += h
    test = [f_linear, f_2nd, f_3rd, f_power, f_log, f_exp]
    i = int(input("Enter id of function: 0-linear, 1-2nd, 2-3nd, 3-power, 4-log, 5-exponent\n"))
    f_i = test[i]
    Y = get_results_array(X, f_i)[1]
    res_or = f_i(x)
    lagr = function_generator(lagrange_function, X, Y)(x)
    newt = function_generator(newton_function, X, Y)(x)
    print("Original = " + str(res_or))
    print("Lagrange = " + str(lagr))
    print("Newton = " + str(newt))

    draw_one_array_one_function(X, Y, function_generator(lagrange_function, X, Y))
    draw_one_array_one_function(X, Y, function_generator(newton_function, X, Y))

if user_input == "in":
    X = enter_float_array("Enter from 8 to 12 numbers (X coordinates)")
    Y = enter_float_array("Enter from 8 to 12 numbers (Y coordinates)")
    if len(X) != len(Y):
        sys.exit("X and Y must have the same size")
    if (len(X) != len(set(X))):
        sys.exit("Repeat of X")
    x = enter_float("Enter x: ")
    lagr = function_generator(lagrange_function, X, Y)(x)
    newt = function_generator(newton_function, X, Y)(x)
    print("Lagrange = " + str(lagr))
    print("Newton = " + str(newt))
    draw_one_array_one_function(X, Y, function_generator(lagrange_function, X, Y))
    draw_one_array_one_function(X, Y, function_generator(newton_function, X, Y))
