class Method:
    def __init__ (self, f, a, b, stop):
        self.f = f
        self.a = a 
        self.b = b 
        self.stop = stop
        self.previous = 0
        self.current = 0
        self.iterations = 0
        
    def calculate(self, variant, func):
        pass