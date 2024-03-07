class Menu:
    def stopChoice(self):
        print("Wybierz kryterium stopu: ")
        print("1. Wariant A - |xi - xi-1| < E")
        print("2. Wariant B - |f(xi)| < E")
        print("3. Liczba iteracji ")
        stop = []
        variant = int(input("Wybor: "))
        stop.append(variant)

        if variant == 1 or variant == 2:
            stop.append(float(input("Podaj epsilon: ")))
            return stop
        elif variant == 3:
            stop.append(int(input("Podaj liczbe iteracji: ")))
            return stop

    def functionChoice(self):
        print("Podaj funkcje:")
        print("1. Funkcja wielomianowa")
        print("2. Funkcja trygonometryczna")
        print("3. Funkcja wykladnicza")
        print("4. Złożenie funkcji")
        func = []
        func.append(int(input("Wybor: ")))

        if func[0] == 1:
            degree = int(input("Podaj stopien wielomianu: "))
            polynomial = []
            for i in range(degree + 1):
                polynomial.append(float(input("Podaj " + str(i + 1) + " wspolczynnik wielomianu: ")))
            func.append(polynomial)
            return func

        elif func[0] == 2:
            print("Wybierz funkcje trygonometryczna:")
            print("1. Sinus")
            print("2. Cosinus")
            print("3. Tangens")
            func.append(int(input("Wybor: ")))
            return func

        elif func[0] == 3:
            func.append(float(input("Podaj podstawe funkcji wykladniczej: ")))
            return func

    def edgesChoice(self):
        print("Wybierz krance przedzialu:")
        edges = []
        edges.append(float(input("Kraniec a: ")))
        edges.append(float(input("Kraniec b: ")))
        return edges