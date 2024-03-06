class Bisekcja:
    def __init__ (self, f, a, b, epsilon):
        self.f = f # funckja ktory liczy wartosc wielomianu
        self.a = a # poczatek przedzialu
        self.b = b # koniec przedzialu
        self.epsilon = epsilon # dokladnosc
        self.previous = 0
        self.iteracje = 0 
    
    def calculate (self, max_iter, variant):
        if variant == 1:
            while((self.b - self.a) / 2 - self.previous) > self.epsilon:
                x = (self.a + self.b) / 2
                if self.f.calculate(x):



        # while (self.b - self.a) / 2 > self.epsilon and self.iteracje < max_iter:
        #     c = (self.a + self.b) / 2
        #     if self.f(c) == 0:
        #         self.iteracje += 1
        #         return c, self.iteracje
        #     elif self.f(c) * self.f(self.a) < 0:
        #         self.b = c
        #     else:
        #         self.a = c
        #     self.iteracje += 1
        # return c, self.iteracje