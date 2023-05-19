import sys
import pandas as pd
from approximation.universal import *
from math_statistics.stats import *
from system_util.IO import *


def generate_resulting_table_arrays(X, Y, functions_array, functions_names_array):
    X = list(X).copy()
    Y = list(Y).copy()
    memory_functions = []
    full_df = pd.DataFrame(
        columns=["Type", "Formula", "Coefficients", "Results", "Ei^2", "Sum(Ei)", "Sigma", "Correlation",
                 "Dependency", "R2"])
    show_df = full_df.drop("Formula", axis=1).drop("Coefficients", axis=1).drop("Ei^2", axis=1).drop(
        "Results", axis=1)
    if len(functions_array) != len(functions_names_array):
        sys.exit("resulting_table_generator arrays must be the same")
    for i in range(len(functions_array)):
        data_of_function = functions_array[i](X.copy(), Y.copy())
        if not (data_of_function[0]):
            continue
        # get type of function
        type_of_function = functions_names_array[i]()[0]
        # get formula
        formula = functions_names_array[i]()[1]
        # get actually new function
        new_function = data_of_function[1]
        # use memory for drawing
        memory_functions.append(new_function)
        # return array of coefficients
        coefficients = data_of_function[2:]
        # return results array
        results = get_results_array(X.copy(), new_function)[1]
        # return array of deviation
        e_array = array_of_deviations_e(Y.copy(), results.copy())
        # and get sum of it
        sum_ei = sum_of_squared_deviations(Y.copy(), results.copy())
        # we must find standard deviation
        sigma = standard_deviation(Y.copy(), results.copy())
        # return covariance
        r = covariance(Y.copy(), results.copy())
        rater_covariance = rate_covariance(r)
        r2 = R2(Y.copy(), results.copy())

        # generate the new lines of data frame
        new_line_full = [type_of_function, formula, str(coefficients), str(results), str(e_array),
                         str(sum_ei), str(sigma), str(r), str(rater_covariance), r2]
        new_line_show = [type_of_function, str(round(sum_ei, 3)), str(round(sigma, 3)), str(round(r, 3)),
                         str(rater_covariance), str(round(r2, 3))]

        full_df.loc[len(full_df)] = new_line_full
        show_df.loc[len(show_df)] = new_line_show

    # sorting data frame by sigma
    full_df = full_df.sort_values(by="Sigma")
    show_df = show_df.sort_values(by="Sigma")
    X, Y1, Y2 = X, Y, get_results_array(X, memory_functions[full_df.index[0]])[1]

    # drawing the graph
    draw_function_one_dot_one_simple_from_array(X, Y1, Y2)
    print(show_df)
    return full_df


def generate_resulting_table_functions(a, b, h, f, functions_array, functions_names_array):
    X, Y = get_results_function(a, b, h, f)
    return generate_resulting_table_arrays(X, Y, functions_array, functions_names_array)
