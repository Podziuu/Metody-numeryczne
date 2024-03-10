class Composite:
    def __init__(self, f1, f2):
        self.f1 = f1
        self.f2 = f2

    def calculate(self, x):
        return self.f1.calculate(self.f2.calculate(x))