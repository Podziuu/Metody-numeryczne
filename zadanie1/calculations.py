class Calculations:
    def __init__(self, indexes):
        self.indexes = indexes
    
    def horner(self, x):
        result = 0
        for i in self.indexes:
            result = result * x + i
        return result
    
    def trigonometry():
        # TODO zrobic obliczenia dla funkcji trygonometrycznych
        print("trigonometry")
        
    def exponential():
        # TODO zrobic obliczenia dla funkcji wykladniczych
        print("exponential")