import matplotlib.pyplot as plt


def sort_data(data):
    data['dots'].sort(key=lambda x: x[0])
    return data


def check_none(results):
    none_methods = []
    for method in results:
        if results[method] is None:
            none_methods.append(method)
    for none_method in none_methods:
        results.pop(none_method)
    return none_methods


def check_results_best_method(results):
    min_sko = float('inf')
    best = None
    for method in results:
        sko = results[method]['standard_deviation']
        if sko < min_sko:
            min_sko = sko
            best = method
    return best


def plot_results(results, data):
    x = [dot[0] for dot in data['dots']]
    y = [dot[1] for dot in data['dots']]
    plt.plot(x, y, 'o', label='Dots')
    for method in results:
        plt.plot(x, results[method]['f(x)'], label=f"{results[method]['string_f']}")
    #legend in left upper corner
    plt.legend(loc='upper left')
    plt.show()
