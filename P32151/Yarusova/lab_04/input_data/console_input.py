def read_dots():
    data = {'dots': []}
    print("Enter dots in format: x y")
    print("Enter 'stop' to stop entering dots")
    while True:
        line = input().strip()
        if line == 'stop':
            if len(data['dots']) < 3:
                print("You must enter at least 3 dots")
                continue
            break
        dot = tuple(map(float, line.split()))
        if len(dot) != 2:
            print("You must enter 2 numbers")
            continue
        data['dots'].append(dot)
    return data
