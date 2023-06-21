import functions


def methodOfRectangle(type, func, a, b, n):
    h = (b - a) / n
    answer = 0
    array = [0] * (n + 1)
    for i in range(n + 1):
        array[i] = a + h * i
    if type == 'left':
        for i in range(n):
            answer += func(array[i])
        answer *= h
    elif type == 'right':
        for i in range(n):
            answer += func(array[i + 1])
        answer *= h
    elif type == 'middle':
        for i in range(n):
            answer += func(array[i] + h / 2)
        answer *= h
    else:
        print("Ashibka")
        exit()
    return answer


def methodOfTrapeze(func, a, b, n):
    h = (b - a) / n
    answer = 0
    array = [0] * (n + 1)
    for i in range(n + 1):
        array[i] = a + h * i
    for i in range(1, n):
        answer += func(array[i])
    answer *= 2
    answer += func(array[0]) + func(array[n])
    answer *= (h / 2)
    return answer


def methodOfSimpson(func, a, b, n):
    h = (b - a) / n
    answer = 0
    array = [0] * (n + 1)
    for i in range(n + 1):
        array[i] = a + h * i
    chet = 0
    nechet = 0
    for i in range(1, n):
        if i % 2 == 0:
            chet += func(array[i])
        else:
            nechet += func(array[i])
    answer = func(array[0]) + func(array[n]) + 2 * chet + 4 * nechet
    answer *= (h / 3)
    return answer
