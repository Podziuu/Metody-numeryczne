class Horner:
    def __init__(self, indexes):
        self.indexes = indexes

    def calculate(self, x):
        result = 0
        for i in self.indexes:
            result = result * x + i
        return result 