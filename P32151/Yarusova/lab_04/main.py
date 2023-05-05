import numpy as np
import matplotlib.pyplot as plt

import input_data
from util import sort_data

input_format = input_data.choose_input_format()
data = {}
if input_format == 1:
    data = input_data.read_dots()
else:
    data = input_data.read_dots_from_file()
data = input_data.sort_data(data)
dots = np.array(data['dots'])
results = {}
results['cube']

