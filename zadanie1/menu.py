from horner import Horner
from trigonometry import Trigonometry
from exponential import Exponential
from composite import Composite

class Menu:
    def stopChoice(self):
        while True:
            print("Wybierz kryterium stopu: ")
            print("1. Wariant A - |xi - xi-1| < E lub Wariant B - |f(xi)| < E")
            print("2. Liczba iteracji ")
            stop = []
            variant = int(input("Wybor: "))
            if variant == 1:
                stop.append(variant)
                while True:
                    epsilon = float(input("Podaj epsilon: "))
                    if epsilon > 0:
                        stop.append(epsilon)
                        return stop
                    else:
                        print("Podaj poprawna liczbe")

            elif variant == 2:
                stop.append(variant)
                while True:
                    iterations = (int(input("Podaj liczbe iteracji: ")))
                    if iterations > 0:
                        stop.append(iterations)
                        return stop
                    else:
                        print("Podaj poprawna liczbe")
            else:
                print("Podaj poprawna opcje")

    def functionChoice(self):
        while True:
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
            else:
                print("Nie ma takiej opcji! Sprobuj jeszcze raz")

    def functionCreator(self):
        while True:
            print("1. Funkcja wielomianowa")
            print("2. Funkcja trygonometryczna")
            print("3. Funkcja wykladnicza")
            choice = int((input("Wybor: ")))

            if choice == 1:
                while True:
                    degree = int(input("Podaj stopien wielomianu: "))
                    if degree > 0:
                        polynomial = []
                        for i in range(degree + 1):
                            polynomial.append(float(input("Podaj " + str(i + 1) + " wspolczynnik wielomianu: ")))
                        return Horner(polynomial)
                    else:
                        print("Podaj prawidlowy stopien wielomianu")

            elif choice == 2:
                while True:
                    print("Wybierz funkcje trygonometryczna:")
                    print("1. Sinus")
                    print("2. Cosinus")
                    print("3. Tangens")
                    fType = (int(input("Wybor: ")))
                    if fType in [1, 2, 3]:
                        return Trigonometry(fType)
                    else:
                        print("Wybierz poprawna opcje")

            elif choice == 3:
                while True:
                    base = (float(input("Podaj podstawe funkcji wykladniczej: ")))
                    if base > 0 and base != 1:
                        return Exponential(base)
                    else:
                        print("Podaj poprawna podstawe")

            else:
                print("Wybierz poprawna opcje")

    def edgesChoice(self):
        print("Wybierz krance przedzialu:")
        edges = []
        edges.append(float(input("Kraniec a: ")))
        edges.append(float(input("Kraniec b: ")))
        return edges