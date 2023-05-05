def read_dots_from_file():
    print("Enter the file name: ")
    file = input()
    f = open(file, 'r')
    data = {'dots': []}
    for line in f:
        dot = tuple(map(float, line.strip().split()))
        if len(dot) != 2:
            print("You must enter 2 numbers for each dot")
            return None
        data['dots'].append(dot)
    if len(data['dots']) < 3:
        print("You must enter at least 3 dots")
        return None
    return data
