import numpy as np

class Jacobi:
    def __init__(self, stop):
        self.stop = stop
        self.iterations = 0

    def isConvergent(self, A):
        for i in range(len(A)):
            rowSum = np.sum(np.abs(A[i])) - np.abs(A[i, i])
            if A[i][i] <= rowSum:
                return False
        return True

    def calculate(self, A, b, variant):
        self.iterations = 0
        if not self.isConvergent(A):
            print("Macierz nie spelnia warunku zbieznosci")
            return None, None
        dimension = len(A)
        accuracyAchieved = False
        x = np.zeros(dimension)

        while True:
            if variant == 1 and accuracyAchieved:
                return x, self.iterations
            xPrevious = np.copy(x)
            for i in range(dimension):
                sum = 0
                for j in range(dimension):
                    sum += A[i, j] * xPrevious[j]
                sum -= A[i, i] * xPrevious[i]
                x[i] = (b[i] - sum) / A[i, i]

            self.iterations += 1
            difference = np.abs(x - xPrevious)
            max_difference = np.max(difference)
            if max_difference < self.stop:
                accuracyAchieved = True

            if variant == 2 and self.iterations >= self.stop:
                return x, self.iterations

