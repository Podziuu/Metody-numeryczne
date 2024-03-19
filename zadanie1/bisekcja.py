from method import Method

class Bisekcja(Method):
    def calculate (self, variant):
        while True:
            self.current = (self.a + self.b) / 2
            
            a_value = self.f.calculate(self.a)
            b_value = self.f.calculate(self.b)
            
            if a_value * b_value >= 0: return "Error"

            current_value = self.f.calculate(self.current)

            if current_value == 0 or (variant == 1 and abs(self.current - self.previous) < self.stop) or (variant == 1 and abs(current_value) < self.stop):
                self.iterations += 1
                return self.current, self.iterations
            

            point_value = self.f.calculate(self.a)
            
            if current_value * point_value < 0:
                self.b = self.current
            else:
                self.a = self.current
            
            self.iterations += 1
            self.previous = self.current
            
            if variant == 2 and self.iterations >= self.stop:
                return self.current, self.iterations