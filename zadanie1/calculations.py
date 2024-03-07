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
        # TODO zrobic obliczenia dla funkcji trygonometrycznych
        print("trigonometry")
        if self.indexes[0] == 1:
            # sin
            return np.sin(x)
        elif self.indexes[0] == 2:
            # cos
            return np.cos(x)
        elif self.indexes[0] == 3:
            # tan
            return np.tan(x)
        
        
    def exponential(self, x):
        # TODO zrobic obliczenia dla funkcji wykladniczych
        print("exponential")
        return self.indexes[0] ** x