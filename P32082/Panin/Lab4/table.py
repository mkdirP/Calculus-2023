import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from approx import *




def mean(V):
    return sum(V)/len(V)


def sum_of_squared_deviations(X_real, X_approx):
    sum = 0
    for i in range(len(X_real)):
        sum += (X_approx[i] - X_real[i]) ** 2
    return sum

def array_of_deviations_e(X_real, X_approx):
    e = []
    for i in range(len(X_real)):
        e.append(X_approx[i] - X_real[i])
    return e

def standard_deviation(X_real, X_approx):
    return sum_of_squared_deviations(X_real, X_approx)/len(X_real)

def covariance(X, Y):
    sum1 = 0
    sum2 = 0
    sum3 = 0
    for i in range(len(X)):
        sum1 += (X[i] - mean(X)) * (Y[i] - mean(Y))
        sum2 += (X[i] - mean(X)) ** 2
        sum3 += (Y[i] - mean(Y)) ** 2
    return sum1/((sum2*sum3)**0.5)

def rate_covariance(r):
    if r < 0.3:
        return "connection is weak"
    if 0.3 <= r < 0.5:
        return "connection is moderate"
    if 0.5 <= r < 0.7:
        return "conspicuous connection"
    if 0.7 <= r < 0.9:
        return "connection is strong"
    if 0.9 <= r <= 1.1:
        return "direct connection"
    else:
        return "Bad value given to rate_covariance!"


def squared_sum(X):
    sum = 0
    for i in range(len(X)):
        sum += X[i] ** 2
    return sum



def generate_table(X, Y, functions_array, functions_names_array):
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
        type_of_function = functions_names_array[i][0]
        formula = functions_names_array[i][1]
        new_function = data_of_function[1]
        memory_functions.append(new_function)
        coefficients = data_of_function[2:]
        results = get_res_arr(X.copy(), new_function)[1]
        e_array = array_of_deviations_e(Y.copy(), results.copy())
        sum_ei = sum_of_squared_deviations(Y.copy(), results.copy())
        sigma = standard_deviation(Y.copy(), results.copy())
        r = covariance(Y.copy(), results.copy())
        rater_covariance = rate_covariance(r)
        r2 = 1 - (sum_of_squared_deviations(Y.copy(), results.copy())) / (squared_sum(results.copy()) - 1 / len(Y.copy()) * (sum(results.copy()) ** 2))

        new_line_full = [type_of_function, formula, str(coefficients), str(results), str(e_array),
                         str(sum_ei), str(sigma), str(r), str(rater_covariance), r2]
        new_line_show = [type_of_function, str(round(sum_ei, 3)), str(round(sigma, 3)), str(round(r, 3)),
                         str(rater_covariance), str(round(r2, 3))]

        full_df.loc[len(full_df)] = new_line_full
        show_df.loc[len(show_df)] = new_line_show

    full_df = full_df.sort_values(by="Sigma")
    show_df = show_df.sort_values(by="Sigma")
    X, Y1, Y2 = X, Y, get_res_arr(X, memory_functions[full_df.index[0]])[1]

    plt.plot(X, Y1, "ro")
    #plt.plot(X, Y2)

    plt.axis([min(X), max(X), min(min(Y1), min(Y2)), max(max(Y1), max(Y2))])
    #plt.show()

    x_interval = np.linspace(min(X)-min(X)/4, max(X)+min(X)/4, 100)
    y_interval = list(map(memory_functions[full_df.index[0]], x_interval))
    plt.plot(x_interval, y_interval)
    plt.axis([min(x_interval)-min(x_interval)/4, max(x_interval)+max(x_interval)/4, min(min(Y), min(y_interval)) - min((min(Y), min(y_interval)))/4, max(max(Y), max(y_interval)) + max((max(Y), max(y_interval)))/4])
    plt.show()






    print(show_df)
    return full_df


def generate_table_handler(a, b, h, f, functions_array, functions_names_array):
    X, Y = get_res_fun(a, b, h, f)
    return generate_table(X, Y, functions_array, functions_names_array)
