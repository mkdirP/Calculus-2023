def read_dots_from_file():
    print("Enter the file name: ")
    file = input()
    f = open(file, 'r')
    data = {'dots': []}
    for line in f:
        if line.strip() == 'stop':
            break
        dot = tuple(map(float, line.strip().split()))
        if len(dot) != 2:
            print("You must enter 2 numbers for each dot")
            return None
        data['dots'].append(dot)
    if len(data['dots']) < 7:
        print("You must enter at least 7 dots")
        return None
    if len(data['dots']) > 12:
        print("You must enter no more than 12 dots")
        data['dots'] = data['dots'][:7]
    return data


def print_results_to_file(results, best):
    file_name = input("Enter the file name: ")
    f = open(file_name, 'w')
    f.write("Results for methods:")
    for method in results:
        f.write(f'{method} = {results[method]}')
    f.write(f'Best method is {best}')
    for item in results[best]:
        if item == 'f':
            continue
        f.write(f'{item} = {results[best][item]}')
    f.close()
