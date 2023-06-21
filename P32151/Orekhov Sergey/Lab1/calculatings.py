SIZE = -1
is_permutation = False

matrixA = [[]]
matrixB = [[]]
matrixX1 = [[]]
matrixX2 = [[]]

epsilon = 0
M = 0


def setMatrixAandB(start_matrix):
    global matrixA, matrixB
    matrixA = [[0] * SIZE] * SIZE
    matrixB = [0] * SIZE

    for i in range(SIZE):
        matrixA[i] = start_matrix[i][0: SIZE]
        matrixB[i] = start_matrix[i][SIZE]

    print("Before:")
    for elem in matrixA:
        print(elem)

    permutationLines()

    print("After:")
    for elem in matrixA:
        print(elem)


def permutationLines():
    for i in range(SIZE):
        searchNormalLine(i)
        if not is_permutation:
            print("НЕ ВЫПОЛНЕНО УСЛОВИЕ О ТОМ ЧТОБЫ ПРИ ЗАМЕНАХ СХОДИЛИСЬ ИТЕРАЦИИ")
            exit()


def searchNormalLine(number):
    global is_permutation
    for i in range(number, SIZE):
        ratio = abs(float(matrixA[i][number]))
        sum_of_others = 0
        for j in range(SIZE):
            sum_of_others += abs(float(matrixA[i][j]))
        sum_of_others -= ratio
        if ratio >= sum_of_others:
            if ratio > sum_of_others:
                is_permutation = True
            shiftLines(number, i)
            return i
    print("Не получается переставить строчки так чтобы выполнилось диагональное преобладание")
    exit()


def shiftLines(i, j):
    global matrixA, matrixB
    matrixA[i], matrixA[j] = matrixA[j], matrixA[i]
    matrixB[i], matrixB[j] = matrixB[j], matrixB[i]


def initX1andX2():
    global matrixX1, matrixX2
    matrixX1 = [0] * SIZE
    matrixX2 = [0] * SIZE
    for i in range(SIZE):
        matrixX2[i] = float(matrixB[i]) / float(matrixA[i][i])


def iteration():
    global matrixX1, matrixX2
    matrixX1 = matrixX2.copy()
    for i in range(SIZE):
        sum_other = 0
        for j in range(SIZE):
            if i > j:
                sum_other += float(matrixA[i][j]) * float(matrixX2[j]) / float(matrixA[i][i])
            elif i < j:
                sum_other += float(matrixA[i][j]) * float(matrixX1[j]) / float(matrixA[i][i])
        matrixX2[i] = float(matrixB[i]) / float(matrixA[i][i]) - sum_other


def checkX():
    for i in range(SIZE):
        if abs(float(matrixX2[i]) - float(matrixX1[i])) > epsilon:
            return False
    return True


def startCalculating():
    count = 0

    while (True):
        iteration()
        count += 1
        if checkX() or count >= M:
            break

    print("После в всех итераций:")
    for i in range(SIZE):
        print("X" + str(i + 1) + " = " + str(matrixX2[i]))

    if count >= M:
        print("Итерации не сходятся(на заданном максимальном их количестве)")
    else:
        print("Общее количество проделанных итераций = " + str(count))

    for i in range(SIZE):
        print("вектор погрешности вектора Х_" + str(i + 1) + " = " + str(abs(matrixX2[i] - matrixX1[i])))
