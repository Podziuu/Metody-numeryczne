from method import Method

class Falsi(Method):    
    def calculate(self, variant):
        while True:
            a_value = self.f.calculate(self.a)
            b_value = self.f.calculate(self.b)
            
            if(a_value * b_value >= 0): return "Error"

            self.current = self.a - (a_value * (self.b - self.a)) / (b_value - a_value)
            
            current_value = self.f.calculate(self.current)
            
            if self.current == 0 or (variant == 1 and abs(self.current - self.previous) < self.stop) or (variant == 1 and abs(current_value) < self.stop):
                self.iterations += 1
                return self.current, self.iterations
            
            if current_value * b_value < 0:
                self.a = self.current
            else:
                self.b = self.current
                
            self.iterations += 1
            self.previous = self.current
            
            if variant == 2 and self.iterations >= self.stop:
                return self.current, self.iterations