def read_dots():
    data = {'dots': []}
    print("Enter dots in format: x y")
    print("Enter 'stop' to stop entering dots")
    while True:
        line = input().strip()
        if line == 'stop':
            if len(data['dots']) < 7:
                print("You must enter at least 7 dots")
                continue
            if len(data['dots']) > 12:
                print("You must enter no more than 12 dots")
                data['dots'] = data['dots'][:7]
            break
        dot = tuple(map(float, line.split()))
        if len(dot) != 2:
            print("You must enter 2 numbers")
            continue
        data['dots'].append(dot)
    return data


def print_results(results, best):
    print("Results for methods:")
    for method in results:
        print(f'{method} = {results[method]}')
    print(f'Best method is {best}')
    for item in results[best]:
        if item == 'f':
            continue
        print(f'{item} = {results[best][item]}')
