from horner import Horner
from trigonometry import Trigonometry
from exponential import Exponential
from composite import Composite

class Menu:
    def stopChoice(self):
        print("Wybierz kryterium stopu: ")
        print("1. Wariant A - |xi - xi-1| < E lub Wariant B - |f(xi)| < E")
        print("2. Liczba iteracji ")
        stop = []
        variant = int(input("Wybor: "))
        stop.append(variant)

        if variant == 1:
            stop.append(float(input("Podaj epsilon: ")))
            return stop
        elif variant == 2:
            stop.append(int(input("Podaj liczbe iteracji: ")))
            return stop

    def functionChoice(self):
        print("Wybierz czy funkcja ma byc zlozona:")
        print("1. Tak")
        print("2. Nie")
        choice = int((input("Wybor: ")))
        if choice == 1:
            f1 = self.functionCreator()
            f2 = self.functionCreator()
            return Composite(f1, f2)
        elif choice == 2:
            return self.functionCreator()

    def functionCreator(self):
        print("1. Funkcja wielomianowa")
        print("2. Funkcja trygonometryczna")
        print("3. Funkcja wykladnicza")
        choice = int((input("Wybor: ")))

        if choice == 1:
            degree = int(input("Podaj stopien wielomianu: "))
            polynomial = []
            for i in range(degree + 1):
                polynomial.append(float(input("Podaj " + str(i + 1) + " wspolczynnik wielomianu: ")))
            return Horner(polynomial)

        elif choice == 2:
            print("Wybierz funkcje trygonometryczna:")
            print("1. Sinus")
            print("2. Cosinus")
            print("3. Tangens")
            fType = (int(input("Wybor: ")))
            return Trigonometry(fType)

        elif choice == 3:
            base = (float(input("Podaj podstawe funkcji wykladniczej: ")))
            return Exponential(base)

    def edgesChoice(self):
        print("Wybierz krance przedzialu:")
        edges = []
        edges.append(float(input("Kraniec a: ")))
        edges.append(float(input("Kraniec b: ")))
        return edges