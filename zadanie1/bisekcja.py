from method import Method

class Bisekcja(Method):
    def calculate (self, variant, func):
        while True:
            self.current = (self.a + self.b) / 2
            if func == 1:
                current_value = self.f.horner(self.current)
            elif func == 2:
                current_value = self.f.trigonometry(self.current)
            elif func == 3:
                current_value = self.f.exponential(self.current)

            if current_value == 0 or (variant == 1 and abs(self.current - self.previous) < self.stop) or (variant == 1 and abs(current_value) < self.stop):
                self.iterations += 1
                return self.current, self.iterations
            
            if func == 1:
                point_value = self.f.horner(self.a)
            elif func == 2:
                point_value = self.f.trigonometry(self.a)
            elif func == 3:
                point_value = self.f.exponential(self.a)
            
            if current_value * point_value < 0:
                self.b = self.current
            else:
                self.a = self.current
            
            self.iterations += 1
            self.previous = self.current
            
            if variant == 2 and self.iterations >= self.stop:
                return self.current, self.iterations