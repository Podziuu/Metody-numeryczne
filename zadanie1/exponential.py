class Exponential:
    def __init__(self, indexes):
        self.indexes = indexes

    def calculate(self, x):
        return self.indexes ** x