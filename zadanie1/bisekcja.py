class Bisekcja:
    def __init__ (self, f, a, b, epsilon):
        self.f = f
        self.a = a 
        self.b = b 
        self.epsilon = epsilon
        self.previous = 0
        self.current = (self.b - self.a) / 2
        self.iterations = 0 

    def calculate (self, variant, max_iter=0):
        while True:
            self.current = (self.a + self.b) / 2
            # TODO zrobic dla innych wartosci w zaleznosci od funkcji
            current_value = self.f.horner(self.current)

            if current_value == 0 or (variant == 1 and abs(self.current - self.previous) < self.epsilon) or (variant == 1 and abs(current_value) < self.epsilon):
                self.iterations += 1
                return self.current, self.iterations
            
            if current_value * self.f.horner(self.a) < 0:
                self.b = self.current
            else:
                self.a = self.current
            
            self.iterations += 1
            self.previous = self.current
            
            if variant == 2 and self.iterations >= max_iter:
                return self.current, self.iterations