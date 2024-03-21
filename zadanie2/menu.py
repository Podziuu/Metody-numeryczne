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
    
    def nOfEquations(self):
        while True:
            n = int(input("Podaj liczbe rownan: "))
            if n > 0 and n < 11:
                return n
            else:
                print("Podaj poprawna liczbe (zakres 1-10)")
    
    def howToLoad(self):
        while True:
            print("Wybierz metode wczytywania:")
            print("1. Z pliku")
            print("2. Z klawiatury")
            choice = int(input("Wybor: "))
            if choice == 1:
                return "file"
            elif choice == 2:
                return "keyboard"
            else:
                print("Podaj poprawna opcje")
                
    def fileLoad(self):
        all_matrices = []
        all_results = []
        while True:
            try:
                filename = input("Podaj nazwe pliku: ")
                with open("zadanie2/" + filename, "r") as file:
                    lines = file.readlines()
                    i = 0
                    while i < len(lines):
                        dimensions = lines[i].split()
                        rows = int(dimensions[0])
                        columns = int(dimensions[1])
                        if rows + 1 != columns:
                            raise ValueError("Macierze musza byc kwadratowa")
                        matrix = []
                        result = []
                        i += 1
                        for _ in range(rows):
                            row = list(map(float, lines[i].split()))
                            matrix.append(row[:rows])
                            result.append(row[-1])
                            i += 1
                        all_matrices.append(matrix)
                        all_results.append(result)
                    return all_matrices, all_results
            except FileNotFoundError:
                print("Nie ma takiego pliku")