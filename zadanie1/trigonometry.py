import numpy as np

class Trigonometry:
    def __init__(self, indexes):
        self.indexes = indexes
    def calculate(self, x):
        if self.indexes == 1:
            return np.sin(x)
        elif self.indexes == 2:
            return np.cos(x)
        elif self.indexes == 3:
            return np.tan(x)