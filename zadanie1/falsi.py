from method import Method

class Falsi(Method):    
    def calculate(self, variant, func):
        while True:
            if func == 1:
                a_value = self.f.horner(self.a)
                b_value = self.f.horner(self.b)
            elif func == 2:
                a_value = self.f.trigonometry(self.a)
                b_value = self.f.trigonometry(self.b)
            elif func == 3:
                a_value = self.f.exponential(self.a)
                b_value = self.f.exponential(self.b)

            self.current = self.a - (a_value * (self.b - self.a)) / (b_value - a_value)
            
            if func == 1:
                current_value = self.f.horner(self.current)
            elif func == 2:
                current_value = self.f.trigonometry(self.current)
            elif func == 3:
                current_value = self.f.exponential(self.current)
            
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