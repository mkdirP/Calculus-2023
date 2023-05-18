import numpy as np

import data_io
import approximation
from util import sort_data
from util import check_none
from util import check_results_best_method
from util import plot_results

input_format = data_io.choose_input_format()
data = {}
if input_format == 1:
    data = data_io.read_dots()
else:
    data = data_io.read_dots_from_file()
data = sort_data(data)
dots = np.array(data['dots'])
results = {'line': approximation.line(dots),
           'square': approximation.square(dots),
           'cube': approximation.cube(dots),
           'exp': approximation.exponenta(dots),
           'pow': approximation.pow(dots),
           'log': approximation.logarithm(dots)}
none_methods = check_none(results)
if len(none_methods) == 6:
    print('All methods returned None')
else:
    print('Methods that returned None: ' + ', '.join(none_methods))
    output_format = data_io.choose_output_format()
    best = check_results_best_method(results)
    if output_format == 1:
        data_io.print_results(results, best)
    else:
        data_io.print_results_to_file(results, best)
plot_results(results, data)
