import system


def read_input_values(x_string, y_string, n):
    x_str = x_string
    y_str = y_string
    x_arr = x_str.split(" ")
    y_arr = y_str.split(" ")
    try:
        x_arr = list(map(float, x_arr))
        y_arr = list(map(float, y_arr))
    except ValueError:
        system.finish_programm("Wrong value")
    if len(x_arr) != len(y_arr) or len(x_arr) != n:
        system.finish_programm("Wrong count of values")
    return [x_arr, y_arr]


def read_int(string):
    x = string
    try:
        n = int(x)
    except(ValueError):
        system.finish_programm("Wrong value")
    return n
