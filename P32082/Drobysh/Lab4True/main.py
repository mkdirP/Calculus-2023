from approximation.cube_approximation import *
from approximation.exponential_approximation import *
from approximation.linear_approximation import *
from approximation.logarithm_approximation import *
from approximation.power_approximation import *
from approximation.square_approximation import *
from functions.functions_lib import *
from tables.data_frame_generator import *
from tables.reader import *


user_input = input("Enter 'file' or 'in' or 'prep'\n")
functions_array = [linear_approximation_from_array, square_approximation_from_array, cube_approximation_from_array,
                   power_approximation_from_array, logarithm_approximation_from_array,
                   exponential_approximation_from_array]
names = [linear_approximation_formula, square_approximation_formula, cube_approximation_formula,
         power_approximation_formula, logarithm_approximation_formula, exponential_approximation_formula]

# input data from file
if user_input == "file":
    df = read_file(input("Enter link\n"))
    generate_resulting_table_arrays(df["X"], df["Y"], functions_array, names).to_csv("answer.csv")

# use prepared functions
if user_input == "prep":
    a, b = enter_interval()
    h = enter_float("Enter h")
    if h >= b - a:
        sys.exit("take smaller h")
    test = [f_from_variant, f_linear, f_2nd, f_3rd, f_power, f_log, f_exp]
    i = int(input("Enter id of function\n"))
    generate_resulting_table_functions(a, b, h, test[i], functions_array, names).to_csv("answer.csv")

#  Input from stdin
if user_input == "in":
    X = enter_float_array("Enter from 8 to 12 numbers (X coordinates)")
    Y = enter_float_array("Enter from 8 to 12 numbers (Y coordinates)")
    if len(X) != len(Y) or (8 > len(X) > 12):
        sys.exit("X and Y must have the same size")
    generate_resulting_table_arrays(X, Y, functions_array, names).to_csv("answer.csv")
