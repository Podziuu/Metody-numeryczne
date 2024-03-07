import numpy as np

class Calculations:
    def __init__(self, indexes):
        self.indexes = indexes
    
    def horner(self, x):
        result = 0
        for i in self.indexes:
            result = result * x + i
        return result
    
    def trigonometry(self, x):
        if self.indexes == 1:
            return np.sin(x)
        elif self.indexes == 2:
            return np.cos(x)
        elif self.indexes == 3:
            return np.tan(x)
        
        
    def exponential(self, x):
        return self.indexes ** x