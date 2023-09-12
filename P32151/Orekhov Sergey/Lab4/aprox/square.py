from gauss import gauss


class Square:
    name = "Square"
    x_array = []
    y_array = []
    phi_array = []
    n = 0
    dm = 0
    sko = 0

    sum_xi = 0
    sum_xi2 = 0
    sum_xi3 = 0
    sum_xi4 = 0

    sum_yi = 0
    sum_xi_yi = 0
    sum_xi2_yi = 0

    a = 0
    b = 0
    c = 0

    def __init__(self, X, Y, N):
        self.x_array, self.y_array = X.copy(), Y.copy()
        self.n = N

    def calculate_sums(self):
        for i in range(self.n):
            self.sum_xi += self.x_array[i]
            self.sum_xi2 += self.x_array[i] ** 2
            self.sum_xi3 += self.x_array[i] ** 3
            self.sum_xi4 += self.x_array[i] ** 4

            self.sum_yi += self.y_array[i]
            self.sum_xi_yi += self.x_array[i] * self.y_array[i]
            self.sum_xi2_yi += self.x_array[i] ** 2 * self.y_array[i]

    def calculate_coeff(self):
        matrix = [[self.sum_xi3, self.sum_xi2, self.sum_xi, self.sum_xi_yi],
                               [self.sum_xi4, self.sum_xi3, self.sum_xi2, self.sum_xi2_yi],
                               [self.sum_xi2, self.sum_xi, self.n, self.sum_yi]]
        gauss_answer = gauss(matrix)
        self.a, self.b, self.c = gauss_answer

    def func(self, x):
        return self.a * x ** 2 + self.b * x + self.c

    def func_string(self):
        return str(self.a) + " * x ** 2 + " + str(self.b) + " * x + " + str(self.c)